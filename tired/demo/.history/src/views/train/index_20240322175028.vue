<template>

    <div>
        <h1>train</h1>
        <el-upload class="upload-demo" action="api//upload/" :on-preview="handlePreview" :on-remove="handleRemove"
            :before-remove="beforeRemove" multiple :limit="3" :on-exceed="handleExceed" :file-list="fileList">
            <el-button size="small" type="primary">点击上传</el-button>
            <div slot="tip" class="el-upload__tip">只能上传excel文件，且不超过500kb</div>
        </el-upload>

        <el-row>
            <el-button type="primary" @click="jump1">模型训练</el-button>
        </el-row>


        <el-row>
            <el-button type="primary" @click="jump2" name="file">模型预测</el-button>
        </el-row>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    data() {
        return {
            tableData: Array(20).fill(item)
        }
    },
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
            axios.get('api/train/model')
                .then(response => {
                    console.log(response);
                })
                .catch(error => {
                    // 处理错误
                    console.error(error);
                });
        },

        jump2() {
            getData().then((data) => {
                console.log(data)
            })
                .catch(error => {
                    // 处理错误
                    console.error(error);
                });
        }

    }
}

</script>