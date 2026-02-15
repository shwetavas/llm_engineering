## AI Text Rewriter with role control

    Please run textrewriter.py. When prompted in the terminal, enter what role you want AI to play (e.g., professional editor, technical writer, or simplifier) in as system prompt and enter the text you want to rewrite as user prompt. The output AI generates depends on the role you set as system_prompt.

## This Project helps to reinforce understanding of:
    1. Correct OpenAI API key usage
    2. Practices system vs user prompt separation
    3. How system prompts control behavior. (i.e the output AI generates)

## Example:

    user_propmt = "The sesquipedalian orator, who was renowned for his prolixity, gesticulated wildly while he was elucidating the intricate esoterica of quantum mechanics, and the perplexed audience, although they were ostensibly engaged, remained utterly confounded."

    system_prompt = simplifier

    Output: 
    
    Here are simplified rewrites of your sentence:

    - The long-winded speaker, famous for his wordiness, waved his arms as he explained the hard, mysterious ideas of quantum mechanics. The audience seemed interested, but they were completely confused.

    - A very talkative speaker, known for using big words, gestured wildly while explaining the tricky ideas in quantum mechanics. The audience looked engaged but stayed utterly confused.

    - The verbose speaker explained hard quantum ideas with wild gestures, and the audience, though attentive, remained confused.

    system_prompt = professional editor

    Output:
    Corrections
    - A very talkative speaker, known for using big words, gestured wildly while explaining.

    Options by tone
    - Neutral/straightforward: A very talkative speaker, known for using big words and gesturing wildly as he explained.
    - Polished: A garrulous speaker renowned for his polysyllabic vocabulary and his exuberant, sweeping gestures as he explained.
    - Vivid/colorful: A supremely loquacious presenter, famed for tossing around grandiloquent words and flailing his arms as he explained.
    - Academic: A highly loquacious orator, noted for an expansive vocabulary and dramatic gesticulation during explanations.
