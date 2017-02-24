#include "dialog.h"
#include "ui_dialog.h"

#include<QSqlDatabase>
#include<QSqlQuery>
#include<QDebug>


bool Dialog::connect_db()
{
    QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE");
    db.setDatabaseName("C:\\develop\\oa\\oa\\database.db");
    if (db.open())
    {
        qDebug()<<"open db success!";
    }
    else
    {
        qDebug()<<"open db failed!";
    }
}

QString Dialog::query_room(QString num)
{
    QString ret ;

    QSqlQuery query;
    query.prepare("select department from room where littletel=:lt1 or littletel2=:lt2");
    query.bindValue(":lt1", num);
    query.bindValue(":lt2", num);
    query.exec();

    if(query.first())
    {
        ret = query.value("department").toString();
    }
    return ret;
}

QString Dialog::query_staff(QString num)
{
    QString ret ;

    QSqlQuery query;
    query.prepare("select name from staff where littlephone=:lp1 or littlephone2=:lp2");
    query.bindValue(":lp1", num);
    query.bindValue(":lp2", num);
    query.exec();

    if(query.first())
    {
        ret = query.value("name").toString();
    }
    return ret;
}

Dialog::Dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);
    connect_db();


}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_numberLineEdit_textChanged(const QString &arg1)
{
    qDebug()<<"==============================";
    qDebug()<<"arg1: "<<arg1;

    QString department = query_room(arg1);
    if (!department.isEmpty())
    {
        ui->nameLabel->setText(department);
    }
    else
    {
        QString name = query_staff(arg1);
        if (!name.isEmpty())
        {
            ui->nameLabel->setText(name);
        }
    }



}
