<template>
  <div class="body">
    <div id="chat-container">
      <div id="chat-messages">
        <div v-for="(message, index) in chatMessages" :key="index" :class="message.type === 'sent' ? 'message sent' : 'message received'">{{ message.text }}</div>
      </div>
      <div id="chat-input">
        <input type="text" v-model="newMessage" @keyup.enter="sendMessage" placeholder="Type your message...">
        <button @click="sendMessage" id="sendButton">Send</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      chatMessages: [],
      newMessage: '',
    };
  },
  methods: {
    sendMessage() {
      if (this.newMessage.trim() !== '') {
        this.chatMessages.push({ text: this.newMessage, type: 'sent' });
        this.getAiResponse(this.newMessage);
        this.newMessage = '';
      }
    },
    async getAiResponse(userInput) {
      // Your AI response fetching logic here
      // This is just a placeholder
      const aiResponse = 'This is the AI response';
      this.chatMessages.push({ text: aiResponse, type: 'received' });
    }
  }
}
</script>

<style scoped>
/* Your existing CSS styles for messages and input can go here */

#chat-messages {
  flex: 1;
  padding: 10px;
  overflow-y: auto;
  background-color: #e6e6e6;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  border-bottom: 1px solid #ccc;
}

#chat-input {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 10px;
  background-color: #f2f2f2;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}

.message.sent {
  float: right;
  background-color: #b3d9ff;
  color: #000;
}

.message.received {
  float: left;
  background-color: #cce6ff;
  color: #000;
}
</style>
