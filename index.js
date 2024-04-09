// REMEMBER TO ADD YOUR API KEY TO THE .env FILE BEFORE RUNNING.
// RUN "node index.js" in the terminal to run this project.

// This imports the new Gemini LLM
import { ChatGoogleGenerativeAI } from '@langchain/google-genai';

// This imports the mechanism that helps create the messages
// called `prompts` we send to the LLM
import { PromptTemplate } from 'langchain/prompts';

// This imports the tool called `chains` that helps combine
// the model and prompts so we can communicate with the LLM
import { LLMChain } from 'langchain/chains';

// This helps connect to our .env file
import * as dotenv from 'dotenv';
dotenv.config();

const template = `Interpret the emotions conveyed by the following emoji(s): {emojis}. Consider each emoji individually and in combination with others in the series. Apply your knowledge of common emoji usage, cultural contexts, and emotional expressions to provide an insightful interpretation. When analyzing multiple emojis, consider the sequence and combination of the emojis to understand any nuanced emotional narrative or sentiment they may collectively express. Additionally, take into account the following considerations:

Emoji Specificity: Identify each emoji and any specific emotions or ideas it typically represents.
Cultural Context: Acknowledge if certain emojis have unique meanings in specific cultural contexts.
Emotional Range: Recognize if emojis express a range of emotions, from positive to negative or neutral.
Sequential Interpretation: When multiple emojis are used, analyze if the sequence changes the overall emotional message.
Complementary and Contrasting Emotions: Note if emojis complement or contrast each other emotionally.
Common Usage Patterns: Reflect on how these emojis are commonly used in digital communication to infer the underlying emotions.
Sarcasm or Irony Detection: Be aware of the possibility of sarcasm or irony in the use of certain emojis.
Emoji Evolution: Consider any recent changes in how these emojis are used or perceived in digital communication.

Based on these guidelines, in one very short sentence, provide a short interpretation of the emotions conveyed by the inputted emoji(s). `;

const promptTemplate = new PromptTemplate({
  template,
  inputVariables: ['emojis'],
});

// Above we created a template variable that contains our
// detailed instructions for the LLM, we also added a
// variable {emojis} which would be replaced with the emojis
// passed in at runtime.
// We then create a prompt template from the template and
// input variable.

// We create our model and pass it a `temperature` of 0.5
// The `temperature` represents how creative we want
// the model to be and it takes values 0.1 - 1
const geminiModel = new ChatGoogleGenerativeAI({
  modelName: 'gemini-pro',
});

// We then use a chain to combine our LLM with our
// prompt template
const llmChain = new LLMChain({
  llm: geminiModel,
  prompt: promptTemplate,
});

// We then call the chain to communicate with the LLM
// and pass in the emojis we want to be explained.
// Note that the property name `emojis` below must match the
// variable name in the template earlier created.
const result = await llmChain.call({
  emojis: '😂🤣',
});

// Log result to the console
console.log(result.text);