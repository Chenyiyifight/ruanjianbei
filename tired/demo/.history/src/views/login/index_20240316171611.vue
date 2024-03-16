<template>
    <div class="back">
        <div class="container">
            <div class="welcome">
                <div class="pinkbox" ref="pinkbox">
                    <div class="signup nodisplay" ref="signup">
                        <h1>注册</h1>
                        <form autocomplete="off">
                            <input type="text" placeholder="账号" v-model="rst.username" />
                            <input type="email" placeholder="邮箱" v-model="rst.email">
                            <input type="password" placeholder="密码" v-model="rst.password" />
                            <input type="password" placeholder="重复密码" v-model="rst.con_password" />
                            <button class="button submit" @click="signup">创建账号</button>
                        </form>
                    </div>
                    <div class="signin" ref="signin">
                        <h1>登录</h1>
                        <form class="more-padding" autocomplete="off">
                            <input type="text" placeholder="账号" v-model="info.username" />
                            <input type="password" placeholder="密码" v-model="info.password" />
                            <div class="checkbox">
                                <input type="checkbox" id="remember" />
                                <label for="remember">记住我</label>
                            </div>
                            <button class="button submit" @click="signin">登录</button>
                        </form>
                    </div>
                </div>
                <div class="leftbox">
                    <h2 class="title">
                        <span>x0</span> <br />
                        系统
                    </h2>
                    <p class="desc">x1<span>登录</span></p>
                    <img class="flower smaller"
                        src="https://img.zcool.cn/community/011b925cdd1a84a801208f8b64b6ea.jpg@2o.jpg" />
                    <p class="account">已有账号</p>
                    <button class="button" @click="showSigninForm">登录</button>
                </div>
                <div class="rightbox">
                    <h2 class="title">
                        <span>x2</span> <br />
                        系统
                    </h2>
                    <p class="desc"><span></span></p>
                    <img class="flower" src="https://img.51miz.com/Element/00/79/11/55/88a77b50_E791155_c8a9c019.png" />
                    <p class="account">还没有账号?</p>
                    <button class="button" @click="showSignupForm">注册</button>
                </div>
            </div>
        </div>
    </div>

</template>


<script>
import axios from "axios";
import Cookie from "js-cookie";
import Mock from 'mockjs'
import { getMenu } from "@/api";

export default {
    data() {
        return {
            info: {
                username: "",
                password: ""
            },
            rst: {
                username: "",
                password: "",
                email: "",
                con_password: ""
            },
        };
    },

    methods: {
        showSignupForm() {
            // 平移盒子，显示注册页面
            this.$refs.pinkbox.style.transform = "translateX(80%)";
            // 隐藏登录表单
            this.$refs.signin.classList.add("nodisplay");
            // 显示注册表单
            this.$refs.signup.classList.remove("nodisplay");
        },
        showSigninForm() {
            // 平移盒子，显示登录页面
            this.$refs.pinkbox.style.transform = "translateX(0%)";
            // 隐藏注册表单
            this.$refs.signup.classList.add("nodisplay");
            // 显示登录表单
            this.$refs.signin.classList.remove("nodisplay");
        },

        // 登录
        signin() {
            console.log(this.info);
            getMenu(this.info).then(response => {
                console.log(response);
                if (response.data.code === 200) {
                    const token = Mock.Random.guid();
                    Cookie.set('token',token);
                    //Cookie.set('token', response.data.data.token)
                    this.$router.push('/home')
                } else {
                    this.$message.error('用户名或密码错误');
                }
            })
        },

        //注册
        signup() {

        }
    }
};
</script>

<style lang="less" scoped></style>
<style scoped>
.back {
    background: rgb(219, 242, 240);
    min-height: 100vh;
}

.container {
    margin: auto;
    width: 650px;
    height: 550px;
    /* 相对定位 */
    position: relative;
}

.welcome {
    background: #fbfafc;
    width: 650px;
    height: 415px;
    /* 绝对定位 */
    position: absolute;
    top: 20%;
    border-radius: 5px;
    box-shadow: 5px 5px 5px rgba(0, 0, 0, 0.1);
}

.pinkbox {
    position: absolute;
    top: -10%;
    left: 5%;
    background: #c8ddf0;
    width: 320px;
    height: 500px;
    border-radius: 5px;
    box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
    /* 慢0.5秒展示 */
    transition: all 0.5s ease-in-out;
    z-index: 2;
}

.nodisplay {
    display: none;
    transition: all 0.5s ease;
}

.leftbox,
.rightbox {
    position: absolute;
    width: 50%;
    transition: all 0.5s ease;
}

.leftbox {
    left: -2%;
}

.rightbox {
    right: -2%;
}

h1 {
    font-family: "Open Sans", sans-serif;
    text-align: center;
    margin-top: 95px;
    color: #f6f6f6;
    font-size: 2em;
    letter-spacing: 8px;
}

.title {
    font-family: "Lora", serif;
    color: #8e9aaf;
    font-size: 1.8em;
    line-height: 1.1em;
    letter-spacing: 3px;
    text-align: center;
    font-weight: 300;
    margin-top: 20%;
}

.desc {
    margin-top: -8px;
}

.account {
    margin-top: 45%;
    font-size: 10px;
}

p {
    font-family: "Open Sans", sans-serif;
    font-size: 0.7em;
    letter-spacing: 2px;
    color: #8e9aaf;
    text-align: center;
}

span {
    color: #eac7cc;
}

.flower {
    position: absolute;
    width: 120px;
    height: 120px;
    top: 43%;
    left: 29%;
    opacity: 0.66;
}

.smaller {
    width: 110px;
    height: 110px;
    top: 48%;
    left: 34%;
    opacity: 0.9;
}

.button {
    padding: 12px;
    font-family: "Open Sans", sans-serif;
    letter-spacing: 3px;
    font-size: 11px;
    border-radius: 10px;
    margin: auto;
    outline: none;
    display: block;
}

.button:hover {
    background: #eac7cc;
    color: #f6f6f6;
    transition: background-color 1s ease-out;
}

.button {
    margin-top: 3%;
    background: #f6f6f6;
    color: #eac7cc;
    border: solid 1px #eac7cc;
}

form {
    display: flex;
    align-items: center;
    flex-direction: column;
    padding-top: 7px;
}

.more-padding {
    padding-top: 35px;
}

.more-padding input {
    padding: 12px;
}

.more-padding .submit {
    margin-top: 45px;
}

.submit {
    margin-top: 25px;
    padding: 12px;
    border-color: #e1c2c6;
}

.submit:hover {
    background: #cbc0d3;
    border-color: #bfb1c9;
}

input {
    background: #edc8cd;
    width: 65%;
    color: #e1e0e0;
    border: none;
    border-bottom: 1px solid rgba(246, 246, 246, 0.5);
    border-radius: 12px;
    padding: 9px;
    margin: 7px;
}

input::placeholder {
    color: #f6f6f6;
    letter-spacing: 2px;
    font-size: 1.3em;
    font-weight: 100;
}

input:focus {
    color: #ce7d88;
    outline: none;
    border-bottom: 1.2px solid rgba(206, 125, 136, 0.7);
    font-size: 1em;
    transition: 0.8s all ease;
}

input:focus::placeholder {
    opacity: 0;
}

label {
    font-family: "Open Sans", sans-serif;
    color: #ce7d88;
    font-size: 0.8em;
    letter-spacing: 1px;
}

.checkbox {
    display: inline;
    white-space: nowrap;
    position: relative;
    left: -62px;
    top: 5px;
}

input[type="checkbox"] {
    width: 7px;
    background: #ce7d88;
}

input[type="checkbox"]:checked+label {
    color: #ce7d88;
    transition: 0.5s all ease;
}
</style>