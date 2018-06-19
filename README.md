# How to control servo with RPI 3
Omar Metwally, MD
```
omar@analog.earth
```

## Connect servo pins using jumper cables and male-female adapters

```
    servo pin  <-->  RPI physical pin
======================================
    red wire		1 (3.3V) or 2 (5V)
    brown wire		6 (GND)
    yellow-orange wire	12 (GPIO18, GPIO_GEN1)
```

yellow-orange wire can be connected to other GPIO pins 

## Control servo via Python
```
    mkdir /home/pi/Desktop/mailsnail
    git init
    git remote add origin https://github.com/osmode/mailsnail.git
    git pull origin master

    cd /home/pi/Desktop/mailsnail
    sudo python3 mailsnail.py
```

## Control servo via command line
```   
    sudo apt-get install -y wiringpi
    gpio -g mode 18 pwm
    gpio pwm-ms
    gpio pwmc 192
    gpio pwmr 2000

    gpio -g pwm 18 100
    gpio -g pwm 18 150
    gpio -g pwm 18 200
```

