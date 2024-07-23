from transformers import AutoModelForSequenceClassification, AutoTokenizer
nli_model = AutoModelForSequenceClassification.from_pretrained('facebook/bart-large-mnli')
tokenizer = AutoTokenizer.from_pretrained('facebook/bart-large-mnli')

premise = '''Microsoft was the first company to participate in the PRISM surveillance program, according to leaked NSA documents obtained by The Guardian and The Washington Post in June 2013, and acknowledged by government secretly access data of non-US citizens hosted by American companies without a warrant. Microsoft has denied participation in such a program.'''
labels = ['R','PG-13','PG','G']
hypothesisR = f'This text is appropriate for children.'
hypothesis13 = f'This text is appropriate for work.'
hypothesisPG = f'This text is text explicit.'
hypothesisG = f'This text is racist.'

hypoList = [hypothesisG,hypothesisPG,hypothesis13,hypothesisR]
count =0
hypoResult = [0] *len(hypoList)
totalProb =0
for hypo in hypoList:
    # run through model pre-trained on MNLI
    x = tokenizer.encode(premise, hypo, return_tensors='pt',
                        truncation_strategy='only_first')
    logits = nli_model(x)[0]

    # we throw away "neutral" (dim 1) and take the probability of
    # "entailment" (2) as the probability of the label being true
    entail_contradiction_logits = logits[:,[0,2]]
    probs = entail_contradiction_logits.softmax(dim=1)
    hypoResult[count] = float(probs[:,1])
    totalProb = totalProb + hypoResult[count]
    count = count+1
#hypoResult = [x / totalProb for x in hypoResult]
print(hypoResult)

