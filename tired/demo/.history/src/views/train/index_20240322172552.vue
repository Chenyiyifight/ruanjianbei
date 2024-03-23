<template>

    <div>
        <h1>train</h1>
        <el-upload class="upload-demo" action="/upload/" :on-preview="handlePreview" :on-remove="handleRemove"
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
import { getData } from '../../api'
export default {
    data() {
        return {
            tableData: Array(20).fill(item),
            fileList: []
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
            if (this.fileList.length > 0) {
                const formData = new FormData();
                formData.append('file', this.fileList[0].raw);

                axios.post('/train/model', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                    .then(response => {
                        console.log(response);
                    })
                    .catch(error => {
                        // 处理错误
                        console.error(error);
                    });
            } else {
                // 处理文件未选择的情况
                this.$message.error('请先选择文件');
            }
        },

        jump2() {
            if (this.fileList.length > 0) {
                const formData = new FormData();
                formData.append('file', this.fileList[0].raw);

                axios.post('/predict/data', formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                })
                    .then(response => {
                        console.log(response);
                    })
                    .catch(error => {
                        // 处理错误
                        console.error(error);
                    });
            } else {
                // 处理文件未选择的情况
                this.$message.error('请先选择文件');
            }
        }

    }
}

</script>