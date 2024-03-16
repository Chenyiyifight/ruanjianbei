<template>
    <div>
        <h1 class="text">forecast</h1>
        <el-row>
            <el-col :span="8" class="anniu">
                <div class="grid-content bg-purple">
                    <div class="n1">
                        <el-button type="primary" round size="mediumsma" @click="StartForecast">开始预测</el-button>
                    </div>
                </div>
            </el-col>
            <el-col :span="16">
                <div class="grid-content bg-purple-light"></div>
            </el-col>
        </el-row>
    </div>
</template>

<script>
import axios from 'axios';
import { getData } from '../../api'

export default {
    data() {
        return {
            f1: 0
        }
    },
    methods: {
        StartForecast() {
            getData().then((data) => {
                console.log(data)
            })
        }

    }
}
</script>

<style scoped>
.grid-content {
    border-radius: 30px;
    min-height: 350px;
}

.bg-purple {
    background: #c6e0fd;
}

.bg-purple-light {
    background: #e5e9f2;
}

.text {
    font-size: 26px;
    margin-left: 10px;
    color: #2d4157;
}

.n1 {
    padding: 150px 100px;
}
</style>