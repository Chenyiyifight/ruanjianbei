<template>
    <div id="chat-container">
        <div id="chat-messages">
            <div class="message received">这里是NDIR博客，内容是如何利用API搭建文心一言AI，你有任何问题吗？</div>
        </div>
        <div id="chat-input">
            <input type="text" id="user-input" placeholder="Type your message...">
            <button onclick="sendMessage()" id="sendButton">Send</button>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {

        }
    },
    methods: {
        async sendMessage() {
            var inputElement = document.querySelector('#user-input');
            var messageText = inputElement.value.trim();
            var sendButton = document.getElementById('sendButton');

            if (messageText !== "") {
                var messagesContainer = document.querySelector('#chat-messages');

                // Display user's message
                var userMessage = document.createElement('div');
                userMessage.className = 'message sent';
                userMessage.textContent = messageText;
                messagesContainer.appendChild(userMessage);

                // Disable send button until AI response
                sendButton.disabled = true;
                // Call AI API
                try {
                    var aiResponse = await getAiResponse(messageText);

                    // Display AI's response with formatted code blocks
                    var aiMessage = document.createElement('div');
                    aiMessage.className = 'message received';
                    aiMessage.innerHTML = formatCodeBlocks(aiResponse.data.result);
                    messagesContainer.appendChild(aiMessage);
                    // Scroll to the bottom
                    messagesContainer.scrollTop = messagesContainer.scrollHeight;
                } catch (error) {
                    console.error("Error fetching AI response:", error);
                }
                // Clear input and enable send button
                inputElement.value = '';
                sendButton.disabled = false;
            }
        },
        async getAiResponse(userInput) {
            var apiUrl = 'https://luckycola.com.cn/ai/openwxyy';

            var requestBody = {
                ques: userInput,
                //替换你的标识
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
            // Match code blocks enclosed in triple backticks (```code ```)
            return text.replace(/```([\s\S]*?)```/g, '<pre>$1</pre>');
        }
    }
}
</script>

<style scoped>
body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    overflow: hidden;
}

#chat-container {
    width: 90%;
    max-width: 400px;
    border: 1px solid #ccc;
    border-radius: 10px;
    overflow: hidden;
    height: 100%;
    display: flex;
    flex-direction: column;
}

#chat-messages {
    flex: 1;
    /* 让消息容器占据剩余空间 */
    padding: 10px;
    overflow-y: auto;
    background-color: #d87878;
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

.el-row {
    margin-bottom: 20px;
}

.el-row:last-child {
    margin-bottom: 0;
}

.bg-purple-dark {
    background: #99a9bf;
}

.bg-purple {
    background: #d3dce6;
}

.bg-purple-light {
    background: #e5e9f2;
}

.grid-content {
    border-radius: 4px;
    min-height: 36px;
}

.row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
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