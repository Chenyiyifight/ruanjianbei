<template>
    <div>
        <h1>show</h1>
        <el-row>
            <el-col :span="8">
                <div class="grid-content bg-purple">
                    <e-charts class="chart" :option="option1" />
                </div>
            </el-col>
            <el-col :span="14">
                <div class="grid-content bg-purple-light">
                    <e-charts class="chart" :option="option2" />
                </div>
            </el-col>
        </el-row>
        <div></div>
    </div>
</template>

<script>
import ECharts from 'vue-echarts';
import 'echarts';

export default {
    components: {
        'e-charts': ECharts,
    },
    data() {
        return {

            option1: {
                xAxis: {
                    type: 'category',
                    data: ['F1']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: [0.9],
                        type: 'bar'
                    }
                ],
            },
            option2: {
                title: {
                    text: 'Referer of a Website',
                    subtext: 'Fake Data',
                    left: 'center'
                },
                tooltip: {
                    trigger: 'item'
                },
                legend: {
                    orient: 'vertical',
                    left: 'left'
                },
                series: [
                    {
                        name: 'Access From',
                        type: 'pie',
                        radius: '50%',
                        data: [
                            { value: 1048, name: 'Search Engine' },
                            { value: 735, name: 'Direct' },
                            { value: 580, name: 'Email' },
                            { value: 484, name: 'Union Ads' },
                            { value: 300, name: 'Video Ads' }
                        ],
                        emphasis: {
                            itemStyle: {
                                shadowBlur: 10,
                                shadowOffsetX: 0,
                                shadowColor: 'rgba(0, 0, 0, 0.5)'
                            }
                        }
                    }
                ]
            }
        }
    }
}
</script>

<style lang="less" scoped>
.chart {
    height: 400px;
    width: 550px;
}
</style>