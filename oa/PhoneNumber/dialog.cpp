#include "dialog.h"
#include "ui_dialog.h"

#include<QSqlDatabase>
#include<QSqlQuery>
#include<QDebug>


bool connect()
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

Dialog::Dialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Dialog)
{
    ui->setupUi(this);
    connect();


}

Dialog::~Dialog()
{
    delete ui;
}

void Dialog::on_numberLineEdit_textChanged(const QString &arg1)
{
    qDebug()<<"==============================";
    qDebug()<<"arg1: "<<arg1;
    QSqlQuery query;


    query.prepare("select * from room where littletel=:lt1 or littletel2=:lt2");
    //query.prepare("select * from room where littletel='66899' or littletel2='66899'");

    query.bindValue(":lt1", arg1);
    query.bindValue(":lt2", arg1);
    query.exec();

    qDebug()<<"is active: "<<query.isActive();
    qDebug()<<"size: "<<query.size();
    //qDebug()<<query.first();

    if(query.first())
    {
        QString name = query.value("department").toString();
        ui->nameLabel->setText(name);
    }
}
