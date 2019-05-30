def imbalanced_class_metrics(train_target,
                             train_preds,
                             test_target,
                             test_preds):
    
    """Show alternative metrics for imbalanced class data.
    Show results of accuracy_score, f1_score, confusion_matrix, 
    classification_report, and roc_auc_score"""
    
    from sklearn.metrics import (accuracy_score,
                             f1_score,
                             confusion_matrix,
                             classification_report,
                             roc_auc_score)
    
    print('Training accuracy: ', accuracy_score(train_preds, train_target), '\n', 
          'Testing accuracy: ', accuracy_score(test_preds, test_target), '\n\n',
          'Classificaiton repot: ', classification_report(test_target, test_preds), '\n',
          'fr score: ', f1_score(test_target, test_preds), '\n', '\n',
          'Confusion Matrix: ', '\n', confusion_matrix(test_target, test_preds), '\n\n',
          'AUC: ', roc_auc_score(test_target, test_preds))
