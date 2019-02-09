#ifndef AGENCE_H
#define AGENCE_H

#include <QMainWindow>

namespace Ui {
class Agence;
}

class Agence : public QMainWindow
{
    Q_OBJECT

public:
    explicit Agence(QWidget *parent = nullptr);
    ~Agence();

private:
    Ui::Agence *ui;
};

#endif // AGENCE_H
