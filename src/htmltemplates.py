css = '''
<style>
.chat-message {
    padding: 0.8rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
    font-size: 0.9rem;
    border: 1px solid #e1e4e8;
}
.chat-message.user {
    background-color: #f9f9f9;
    justify-content: end;
}
.chat-message.bot {
    background-color: #f9f9f9;
    justify-content: start;
}
.chat-message .avatar img {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    object-fit: cover;
    margin: 0 10px;
}
.chat-message .message {
    padding: 0.5rem 1rem;
    color: #333;
    background-color: #eef2f7;
    border-radius: 15px;
    max-width: 80%;
    word-wrap: break-word;
}
.stButton>button {
        color: white;
        background-color: #f63366;
        border-radius: 5px;
        border: 1px solid #4CAF50;
    }
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="img/bot.png" alt="Bot">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="message">{{MSG}}</div>
    <div class="avatar">
        <img src="img/user.png" alt="User">
    </div>    
</div>
'''