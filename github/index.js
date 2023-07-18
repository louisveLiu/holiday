import { Configuration, OpenAIApi } from "openai";
import express from "express";
import bodyParser from "body-parser";
import cors from "cors";

const configuration = new Configuration({
    organizationId: "org-nßy7oM9eWvBTHN5zoMNDKrWWe",
    apiKey: "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",
});

const openai = new OpenAIApi(configuration);

const app = express();
const port = 3000;

app.use(bodyParser.json());
app.use(cors());

app.post("/", async (req, res) => {

    const {message} = req.body;

    console.log(message);
    const completion = await openai.createChatCompletion({
        model:"gpt-3.5-turbo",
        messages: [
            {"role":"system", "content": "You are a DesignGPT helpful assistant graphics design chatbot"},
            ...messages
            //{role:"user", content: '${message}'},
        ]
    })

    res.json({
        completion: completion.data.choices[0].message
    })
});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
});
