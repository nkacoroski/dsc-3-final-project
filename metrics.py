import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import (f1_score,
                             precision_recall_curve,
                             auc,
                             average_precision_score,
                             roc_curve,
                             confusion_matrix)

def print_metrics(model, X_train, X_test, y_train, y_test):
    """Print f1 score, auc, average precision and return
    roc curve and precision-recall curve for training and test data"""
    model.fit(X_train, y_train)
    train_prob = model.predict_proba(X_train)
    test_prob = model.predict_proba(X_test)
    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)
    
    f1_train = np.round(f1_score(y_train, train_pred, labels=np.unique(train_pred)), 2)
    f1_test = np.round(f1_score(y_test, test_pred, labels=np.unique(test_pred)), 2)

    precision_train, recall_train, thresholds_train = precision_recall_curve(y_train, train_prob[:,1])
    precision_test, recall_test, thresholds_test = precision_recall_curve(y_test, test_prob[:,1])
    auc_train = np.round(auc(recall_train, precision_train), 3)
    auc_test = np.round(auc(recall_test, precision_test), 3)

    ap_train = np.round(average_precision_score(y_train, train_prob[:,1]), 3)
    ap_test = np.round(average_precision_score(y_test, test_prob[:,1]), 3)

    fpr, tpr, thresholds = roc_curve(y_train, train_prob[:,1])
    test_fpr, test_tpr, test_thresholds = roc_curve(y_test, test_prob[:,1])
    
    print('\n',
          'Train', '\n',
          'F1 Score: ', f1_train, '\n',
          'Average Precision: ', ap_train, '\n',
          'AUC: ', auc_train, '\n\n',
          'Confusion Matrix: ', '\n', confusion_matrix(y_train, train_pred), '\n\n',
          'Test', '\n',
          'F1 Score: ', f1_test, '\n',
          'Average Precision: ', ap_test, '\n',
          'AUC: ', auc_test, '\n\n',
          'Confusion Matrix: ', '\n', confusion_matrix(y_test, test_pred), '\n\n')

    return graph_metrics(y_train, train_prob, y_test, test_prob)
    
    
def graph_metrics(y_train, train_prob, y_test, test_prob):
    """Graph roc curve, precision recall curve, histogram of 
    target test data predicted probabilities, and scatter plot 
    of target test actual values and predicted probabilities"""
    
    fpr_train, tpr_train, thresholds = roc_curve(y_train, train_prob[:,1])
    fpr_test, tpr_test, test_thresholds = roc_curve(y_test, test_prob[:,1])
    precision_train, recall_train, train_thresholds = precision_recall_curve(y_train, train_prob[:,1])
    precision_test, recall_test, thresholds = precision_recall_curve(y_test, test_prob[:,1])
    
    target_df = y_test.to_frame()
    target_df.tail()
    target_df['y_pred'] = test_prob[:,1]
    
    
    sns.set()
    sns.set_style("white", {"xtick.bottom":True, "ytick.left":True})
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12,10))
    
    ax1.plot([0,1],[0,1], linestyle='--', color='k', label='no skill')
    ax1.plot(fpr_train, tpr_train, label='train', color='green')
    ax1.plot(fpr_test, tpr_test, label='test', color='gold')
    ax1.set_xlabel('Specificity (False Positive Rate)')
    ax1.set_ylabel('Sensitivity (True Positive Rate)')
    ax1.set_title('ROC Curve')

    ax2.plot([0,1], [0.1,0.1], linestyle='--', color='k', label='no skill')
    ax2.plot(recall_train, precision_train, label='train', color='green')
    ax2.plot(recall_test, precision_test, label='test', color='gold')
    ax2.set_xlabel('Recall (Sensitivity)')
    ax2.set_ylabel('Precision (Positive Predictive Value)')
    ax2.set_title('Precision-Recall Curve')
    ax2.legend()
    
    ax3.hist(test_prob[:,1], color='green', alpha=.5)
    ax3.set_xlabel('Probability')
    ax3.set_ylabel('Count')
    ax3.set_title('Predicted Probabilities Counts')
    
    ax4.scatter(target_df['invasive'], target_df['y_pred'], color='green',
                alpha=.5)
    ax4.set_xlabel('Actual Values')
    ax4.set_ylabel('Predicted Probabilities')
    ax4.set_title('Actual Values and Predicted Probabilities')
    
    
    sns.despine()
    plt.tight_layout()
    plt.show();