const express = require("express");
const path = require("path");
const TelegramBot = require("node-telegram-bot-api");
const TOKEN = "7329064759:AAHDQxmRDtiie1o27T_Z-DFMIJnM-5RRcSE";
const server = express();
const bot = new TelegramBot(TOKEN, {
    polling: true
});
const port = process.env.PORT || 5000;
const gameName = "DinoTon";
const queries = {};
server.use(express.static(path.join(__dirname, 'DinoTonClicker')));
bot.onText(/help/, (msg) => bot.sendMessage(msg.from.id, "Say /game if you want to play."));
//bot.onText(/start/, (msg) => {
//    bot.sendGame(msg.from.id, gameName));
//    chatId = msg.chat.id;
//}
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  const gameUrl = 'https://samirshef.github.io/DinoTonClicker/?telegramId=${chatId}';

  const options = {
    reply_markup: JSON.stringify({
      inline_keyboard: [
        [{text: 'Играть', callback_game: JSON.stringify({game_short_name: 'DinoTon'})}]
      ]
    })
  };

  bot.sendMessage(chatId, 'Нажмите кнопку ниже, чтобы начать игру!', options);
});
bot.on('callback_query', function onCallbackQuery(callbackQuery) {
  const action = callbackQuery.data;
  const msg = callbackQuery.message;
  const opts = {
    chat_id: msg.chat.id,
    message_id: msg.message_id,
    game_short_name: 'DinoTon'
  };
  bot.answerCallbackQuery(callbackQuery.id, opts);
});
bot.on("inline_query", function (iq) {
    bot.answerInlineQuery(iq.id, [{
        type: "game",
        id: "0",
        game_short_name: gameName
    }]);
});
server.get("/highscore/:score", function (req, res, next) {
    if (!Object.hasOwnProperty.call(queries, req.query.id)) return next();
    let query = queries[req.query.id];
    let options;
    if (query.message) {
        options = {
            chat_id: query.message.chat.id,
            message_id: query.message.message_id
        };
    } else {
        options = {
            inline_message_id: query.inline_message_id
        };
    }
    bot.setGameScore(query.from.id, parseInt(req.params.score), options,
        function (err, result) {});
});
server.listen(port);
