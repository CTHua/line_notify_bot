# Line Notify Bot

Use line notify bot to send message to line group.

## Usage

Modify file named `keys.json`

```json
{
  "group_name_1": "your_token_1",
  "group_name_2": "your_token_2",
  "group_name_3": "your_token_3"
}
```

And define your data with name: `today date.json` e.g. `20220503.json`

```json
{
  "公告": "公告內容",
  "blocks": [
    {
      "head_1": "message_line_1",
      "head_2": "message_line_2"
    },
    {
      "head_3": "message_line_3",
      "head_4": "message_line_4"
    }
  ],
  "提醒": "提醒內容"
}
```

then message will look like this:

```plaintext
bot_name 公告內容
head_1 message_line_1
head_2 message_line_2
(blank line)
head_3 message_line_3
head_4 message_line_4
(blank line)
提醒內容
```

then run

````bash
python line_notify_bot.py
````
