### STM32电压和电流的设计规范

![1697876598433](image/voltageAndCurrentRules/1697876598433.png)

![1697876800534](image/voltageAndCurrentRules/1697876800534.png)

### Special Notions

1. VDDA我们有的时候使用高精度的稳压器芯片来做稳压，比如REF3030，但是要注意Vdd和Vdda之间的电压差不能超过0.4V
2. 电流的话，整个芯片的电流其实是100mA的量级
