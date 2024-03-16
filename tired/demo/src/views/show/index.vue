<template>
    <div>
        <h1>show</h1>
        <e-charts class="chart" :option="option" />
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
            
            option: {
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
            }
        }
    }
}
</script>

<style lang="less" scoped>
.chart {
    height:400px;
    width: 550px;
}
</style>