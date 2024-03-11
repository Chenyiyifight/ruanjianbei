<template>
    <el-row>
        <el-col :span="8">
            <el-card class="box-card">
                <div class="user">
                    <img src="../assets/images/user.png" alt="">
                    <div class="userinfo">
                        <p class="name">Admin</p>
                        <p class="access">超级管理员</p>
                    </div>
                </div>
                <div class="login-info"></div>
            </el-card>

        </el-col>
        <el-col :span="16">
            <e-charts class="chart" :option="option" />
        </el-col>
    </el-row>
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
.user {
    display: flex;
    align-items: center;

    img {
        margin-right: 40px;
        width: 150px;
        height: 150px;
        border-radius: 50%;
    }

    .userinfo {
        font-size: 20px;
        margin-bottom: 10px;
    }
}

.chart {
    height: 400px;
    font-weight: 10px;
}
</style>