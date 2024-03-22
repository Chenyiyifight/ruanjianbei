<template>
    <div class="body">
        <div id="chat-container">
            <div id="chat-messages">
                <div class="message received">我是AI小助手🤡</div>
            </div>
            <div id="chat-input">
                <input type="text" id="user-input" placeholder="Type your message...">
                <button @click="sendMessage" id="sendButton">Send</button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    methods: {
        async sendMessage() {
            var inputElement = document.querySelector('#user-input');
            var messageText = inputElement.value.trim();
            var sendButton = document.getElementById('sendButton');

            if (messageText !== "" && !sendButton.disabled) {
                sendButton.disabled = true; // 禁用发送按钮

                try {
                    var aiResponse = await this.getAiResponse(messageText);

                    // 显示AI回复
                    this.displayAiResponse(aiResponse.data.result);
                } catch (error) {
                    console.error("Error fetching AI response:", error);
                }

                // 启用发送按钮
                sendButton.disabled = false;
                inputElement.value = ''; // 清空输入框
            }
        },

        async getAiResponse(userInput) {
            var apiUrl = 'https://luckycola.com.cn/ai/openwxyy';
            var requestBody = {
                ques: userInput,
                appKey: "65f81c418dac29f464443498",
                uid: "ibrgkb1710758856457eVNxhZnLBG",
                isLongChat: 0
            };

            var response = await fetch(apiUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(requestBody),
            });

            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Failed to fetch AI response');
            }
        },

        formatCodeBlocks(text) {
            var tempDiv = document.createElement('div');
            tempDiv.textContent = text;
            return tempDiv.innerHTML;
        }

    }
}
</script>

<style scoped>
.body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    background-color: rgba(255, 255, 255, 0);
    display: flex;
    align-items: center;
    justify-content: center;
    height: 500px;
    width: 30%;
    overflow: hidden;
}

#chat-container {
    width: 98%;
    max-width: 290px;
    border: 1px solid #e2e0f7;
    border-radius: 10px;
    overflow: hidden;
    height: 100%;
    display: flex;
    flex-direction: column;
}

#chat-messages {
    flex: 1;
    /* 让消息容器占据剩余空间 */
    padding: 20px;
    overflow-y: auto;
    background-color: #e2e0f7;
}

.message {
    clear: both;
    padding: 8px;
    margin-bottom: 8px;
    border-radius: 5px;
    max-width: 70%;
    word-wrap: break-word;
}

.message.sent {
    float: right;
    background-color: #4caf50;
    color: #fff;
}

.message.received {
    float: left;
    background-color: #e0e0e0;
}

#chat-input {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 10px;
    background-color: #fff;
    border-top: 1px solid #ccc;
}

#chat-input input {
    flex: 1;
    padding: 8px;
    margin-right: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

#chat-input button {
    padding: 8px;
    border: none;
    border-radius: 5px;
    background-color: #4caf50;
    color: #fff;
    cursor: pointer;
}

#chat-input button:disabled {
    background-color: #ccc;
    cursor: not-allowed;
}
</style>