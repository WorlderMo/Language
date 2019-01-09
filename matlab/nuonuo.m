%常住人口（单位：万人）
numberOfPeople=[52.3 53.6 54.4 55.5];
%地区生产总值（单位：亿元）
grp=[225.84 234.71 245.32 313.72];
%固定资产投资总额（单位：亿元）
investment=[160 161.03 226.92 271.76 ];
%社会消费品零售总额（单位：亿元）
retailSales=[62.49 67.04 77.01 101.5];
%城镇居民人均可支配收入（单位：元）
income=[36344 33355 35719 38688];
%地方财政（单位：亿元）
localFinance=[38.81 48.82 50.03 60.86];
%地区面积（目标数据）
area=[100 110 120 130];

%第五年用来做测试数据
input_test=[58.1 378.8 334.29 209.94 42330 74.67];
output_test=14;

%输入数据矩阵
inputData=[numberOfPeople; grp; investment; retailSales; income; localFinance];
%目标（预测）数据矩阵
outputData=area;


%对训练集中的输入数据矩阵和目标数据矩阵进行归一化处理
[pn, inputStr] = mapminmax(inputData);
[tn, outputStr] = mapminmax(outputData);

%建立BP神经网络
net = newff(pn, tn, [6 7 1], {'purelin', 'logsig', 'purelin'}, 'trainlm');



%网络的学习速率
net.trainParam.lr = 0.1;
%最大训练次数
net.trainParam.epochs = 5000;
%训练网络允许目标误差
net.trainParam.goal = 0.000001;
%网络误差如果连续6次迭代都没变化，则matlab会默认终止训练。为了让程序继续运行，用以下命令取消这条设置
net.divideFcn = '';

%开始训练网络
net = train(net, pn, tn);

%使用训练好的网络，基于训练集的数据对BP网络进行仿真得到网络输出结果
answer = sim(net, pn)

%反归一化
answer1 = mapminmax('reverse', answer, outputStr)






