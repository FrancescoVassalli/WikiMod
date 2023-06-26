# WikiMod
This is demo tool for classifying wikipedia pages on the G,PG,PG-13, R or explicit scale. To run this rool you need an Open AI account and API key as well as python. I except your API key to be stored in the environment variable OPEN_API_KEY. Then you can pull this code and run it with:  
```python model.py wikiname```  
Where wikiname is the exact name of the wikipedia page in the url like 2022_in_video_games .  
This will return a raw API result such as: 
```
{
  "id": "chatcmpl-7VWhvF5JoyrLX5fNSOzO6LG6DNb2r",
  "object": "chat.completion",
  "created": 1687748251,
  "model": "gpt-3.5-turbo-0301",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Rating: PG\n\nReasoning: The article discusses the video game industry and its developments in 2022, including the effects of the COVID-19 pandemic, hardware sales, and acquisitions and mergers. It also mentions issues such as workplace harassment and discrimination, as well as crunch periods. The article briefly touches on the 2022 Russian invasion of Ukraine and how some video game developers and publishers provided support for Ukrainian aid. The article does not contain any explicit language or graphic content, but some of the topics discussed may not be suitable for young children."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 794,
    "completion_tokens": 111,
    "total_tokens": 905
  }
}
```
