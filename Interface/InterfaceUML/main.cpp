#include "agence.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Agence w;
    w.show();

    return a.exec();
}
