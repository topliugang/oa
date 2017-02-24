#ifndef DIALOG_H
#define DIALOG_H

#include <QDialog>

namespace Ui {
class Dialog;
}

class Dialog : public QDialog
{
    Q_OBJECT

public:
    explicit Dialog(QWidget *parent = 0);
    ~Dialog();

private slots:
    void on_numberLineEdit_textChanged(const QString &arg1);

private:
    Ui::Dialog *ui;
    bool connect_db();
    QString query_room(QString num);
    QString query_staff(QString num);
};

#endif // DIALOG_H
