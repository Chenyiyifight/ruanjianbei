<template>

    <div>
        <h1>train</h1>
        <div> <el-upload class="upload-demo" action="http://localhost:8000/api/upload/" :on-preview="handlePreview"
                :on-remove="handleRemove" :before-remove="beforeRemove" multiple :limit="3" :on-exceed="handleExceed"
                :file-list="fileList">
                <el-button size="small" type="primary">点击上传</el-button>
                <div slot="tip" class="el-upload__tip">只能上传excel文件，且不超过500kb</div>
            </el-upload>

            <div class="container">
                <el-select v-model="value" placeholder="请选择" class="item">
                    <el-option v-for="item in tOptions" :key="item.value" :label="item.label" :value="item.value">
                    </el-option>
                </el-select>
                <el-row class="item">
                    <el-button type="primary" @click="jump1">模型训练</el-button>
                </el-row>
            </div>
            <el-row>
                <el-button type="primary" @click="jump2" name="file">模型预测</el-button>
            </el-row>
        </div>

        <e-charts class="chart" :option="option" />

    </div>
</template>

<script>
import axios from 'axios';
import { getData } from '../../api'
import { trainMo } from '../../api'
import ECharts from 'vue-echarts';
import 'echarts';

export default {
    components: {
        'e-charts': ECharts,
    },
    data() {
        return {
            option: {
                title: {
                    text: 'Stacked Line'
                },
                tooltip: {
                    trigger: 'axis'
                },
                legend: {
                    data: ['Email', 'Union Ads', 'Video Ads', 'Direct', 'Search Engine']
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                toolbox: {
                    feature: {
                        saveAsImage: {}
                    }
                },
                xAxis: {
                    type: 'category',
                    boundaryGap: false,
                    data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        name: 'Email',
                        type: 'line',
                        stack: 'Total',
                        data: [120, 132, 101, 134, 90, 230, 210]
                    },
                    {
                        name: 'Union Ads',
                        type: 'line',
                        stack: 'Total',
                        data: [220, 182, 191, 234, 290, 330, 310]
                    },
                    {
                        name: 'Video Ads',
                        type: 'line',
                        stack: 'Total',
                        data: [150, 232, 201, 154, 190, 330, 410]
                    },
                    {
                        name: 'Direct',
                        type: 'line',
                        stack: 'Total',
                        data: [320, 332, 301, 334, 390, 330, 320]
                    },
                    {
                        name: 'Search Engine',
                        type: 'line',
                        stack: 'Total',
                        data: [820, 932, 901, 934, 1290, 1330, 1320]
                    }
                ]
            },
            tOptions: [{
                value: '选项1',
                label: '黄金糕'
            }, {
                value: '选项2',
                label: '双皮奶'
            }, {
                value: '选项3',
                label: '蚵仔煎'
            }, {
                value: '选项4',
                label: '龙须面'
            }, {
                value: '选项5',
                label: '北京烤鸭'
            }],
            value: ''
            
        }
    },
    //tableData: Array(20).fill(item),

    methods: {
        handleRemove(file, fileList) {
            console.log(file, fileList);
        },
        handlePreview(file) {
            console.log(file);
        },
        handleExceed(files, fileList) {
            this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
        },
        beforeRemove(file, fileList) {
            return this.$confirm(`确定移除 ${file.name}？`);
        },


        jump1() {

            trainMo()
                .then(response => {
                    console.log(response);
                })
                .catch(error => {
                    // 处理错误
                    console.error(error);
                });
        },

        jump2() {
            getData()
                .then(response => {
                    console.log(response);
                })
                .catch(error => {
                    // 处理错误
                    console.error(error);
                });
        }

    },
    mounted() {
        this.initChart();
    }
}

</script>

<style scoped>
.chart {
    height: 400px;
    width: 70%;
    margin-top: 30px;
}

.container {
    display: flex;
    justify-content: flex-start;
    margin-bottom: 20px;
    margin-top: 20px;
}

.item {
    margin-right: 20px;
}

/* 最后一个元素去掉右边距 */
.item:last-child {
    margin-right: 0;
}
</style>