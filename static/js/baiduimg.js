 function fenxi() {
 	// 基于准备好的dom，初始化echarts实例 	
 	var myChart = echarts.init(document.getElementById("container"));
 	var data01 = [320, 332, 301, 334, 390, 1000, 1300, 1000, 800, 600, 500, 200];
 	var data02 = [220, 182, 191, 234, 290, 850, 1200, 900, 700, 500, 400, 100];
 	// 指定图表的配置项和数据
 	var option = {
 		color: ['#e5323e', '#006699'],
 		tooltip: {
 			trigger: 'axis',
 			axisPointer: {
 				type: 'shadow'
 			}
 		},
 		legend: {
 			data: ['Forest', 'Steppe']
 		},
 		toolbox: {
 			show: true,
 			orient: 'vertical',
 			left: 'right',
 			top: 'center',
 			feature: {
 				mark: {
 					show: true
 				},
 				dataView: {
 					show: true,
 					readOnly: false
 				},
 				magicType: {
 					show: true,
 					type: ['line', 'bar', 'stack', 'tiled']
 				},
 				restore: {
 					show: true
 				},
 				saveAsImage: {
 					show: true
 				}
 			}
 		},
 		calculable: true,
 		xAxis: [{
 			type: 'category',
 			axisTick: {
 				show: false
 			},
 			data: ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月']
 		}],
 		yAxis: [{
 			type: 'value'
 		}],
 		series: [{
 				name: 'Forest',
 				type: 'bar',
 				barGap: 0,
 				//label: labelOption,
 				data: data01
 			},
 			{
 				name: 'Steppe',
 				type: 'bar',
 				//label: labelOption,
 				data: data02
 			}
 		]
 	};
 	// 使用刚指定的配置项和数据显示图表。
 	myChart.setOption(option);
 }