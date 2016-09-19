import os
import sys
from bottle import route, run, template, request
from gensim.models import word2vec

@route('/')
def index():
    frm = """
        <h1>Word2Vecを使って、あるお店の口コミを解析したものです。</h1>
        <h3>キーワードを入力すると、関連の強い単語を口コミ内から探し、関連の強い順に表示します。</h3>
        <h3>(例：「料理」、「山菜」、「柚子」、「炭火」、「海老」...)</h3>
        <h4 style="color: red;">※関連する単語がない場合Internal Server Error起こるけど気にしないで</h4>
        <form action="/w2v" method="post">
            <p><input type="text" name="word" width="50"></input></p>
            <p><input type="submit" value="   関連する単語を探す   " /></p>
        </form>
    """
    return template(frm)

@route('/w2v', method="POST")
def sum():
    word = request.forms.decode().get("word")
    print(word)

    sumres = model.most_similar(positive=[word])
    out = """
        <h1>関連の強い単語</h1>
        <p>{{sumres}}</p>
    """
    return template(out, word=word, sumres=sumres)

if __name__ == "__main__":
    data = word2vec.Text8Corpus('data.txt')
#    model = word2vec.Word2Vec(data, size=200, min_count=10, window=10)
    model = word2vec.Word2Vec(data, size=200)

    run(host='0.0.0.0', port=8081, reloader=True)

