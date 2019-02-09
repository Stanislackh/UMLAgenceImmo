#include "agence.h"
#include "ui_agence.h"

Agence::Agence(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::Agence)
{
    ui->setupUi(this);
}

Agence::~Agence()
{
    delete ui;
}
