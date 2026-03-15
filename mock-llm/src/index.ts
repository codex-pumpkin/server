import express from "express";

const app = express();
app.use(express.json());

app.post("/v1/chat/completions", (req, res) => {
    res.json({
        id: "chatcmpl-mock",
        object: "chat.completion",
        created: Math.floor(Date.now() / 1000),
        model: "gpt-5.4",
        choices: [
            {
                index: 0,
                message: {
                    role: "assistant",
                    content:
                        " * Simple RC circuit\n" +
                        "V1 1 0 DC 5\n" +
                        "R1 1 2 1k\n" +
                        "C1 2 0 1u\n" +
                        "R2 2 0 1meg\n" +
                        ".TRAN 10u 10m\n" +
                        ".PRINT TRAN V(1) V(2) I(V1)\n" +
                        ".END "
                },
                finish_reason: "stop"
            }
        ],
        usage: {
            prompt_tokens: 10,
            completion_tokens: 20,
            total_tokens: 30
        }
    });
});

app.listen(5555, "0.0.0.0", () => {
    console.log("Mock OpenAI endpoint running on http://localhost:5555");
});