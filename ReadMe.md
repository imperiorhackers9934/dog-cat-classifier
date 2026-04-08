
<style>
  body { margin: 0; padding: 0; }
  .readme { font-family: var(--font-sans); color: var(--color-text-primary); max-width: 860px; padding: 2rem 1.5rem; }
  .hero { border-radius: var(--border-radius-lg); padding: 2rem 2rem 1.5rem; margin-bottom: 2rem; background: linear-gradient(135deg, #a5b294 0%, #91a8bd 50%, #b19e7e 100%); border: 0.5px solid var(--color-border-tertiary); position: relative; overflow: hidden; }
  .hero-emoji { font-size: 48px; line-height: 1; margin-bottom: 0.75rem; display: block; }
  .hero h1 { font-size: 26px; font-weight: 500; margin: 0 0 0.5rem; color: var(--color-text-primary); }
  .hero p { font-size: 15px; color: var(--color-text-secondary); margin: 0; line-height: 1.6; }
  .tags { display: flex; flex-wrap: wrap; gap: 8px; margin-top: 1rem; }
  .tag { font-size: 12px; padding: 4px 10px; border-radius: 100px; font-weight: 500; }
  .tag-green { background: #C0DD97; color: #27500A; }
  .tag-blue { background: #B5D4F4; color: #0C447C; }
  .tag-amber { background: #FAC775; color: #633806; }
  .tag-purple { background: #CECBF6; color: #3C3489; }

  .stats-grid { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; margin-bottom: 2rem; }
  .stat-card { background: var(--color-background-secondary); border-radius: var(--border-radius-md); padding: 1rem; text-align: center; }
  .stat-label { font-size: 12px; color: var(--color-text-secondary); margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.04em; }
  .stat-value { font-size: 22px; font-weight: 500; color: var(--color-text-primary); }
  .stat-sub { font-size: 12px; color: var(--color-text-secondary); margin-top: 2px; }

  .section { margin-bottom: 2rem; }
  .section-title { font-size: 16px; font-weight: 500; color: var(--color-text-primary); margin: 0 0 1rem; display: flex; align-items: center; gap: 8px; }
  .section-title span { font-size: 16px; }

  .feature-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
  .feature-card { background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-md); padding: 12px 14px; display: flex; align-items: flex-start; gap: 10px; }
  .feature-icon { font-size: 18px; flex-shrink: 0; }
  .feature-text { font-size: 13px; color: var(--color-text-secondary); line-height: 1.5; }
  .feature-text strong { font-weight: 500; color: var(--color-text-primary); display: block; margin-bottom: 2px; }

  .arch-card { background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: 1.25rem; }
  .arch-row { display: flex; justify-content: space-between; align-items: center; padding: 8px 0; border-bottom: 0.5px solid var(--color-border-tertiary); font-size: 14px; }
  .arch-row:last-child { border-bottom: none; padding-bottom: 0; }
  .arch-row .key { color: var(--color-text-secondary); }
  .arch-row .val { font-weight: 500; }

  .predictions { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
  .pred-card { background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); overflow: hidden; }
  .pred-img { width: 100%; height: 120px; display: flex; align-items: center; justify-content: center; font-size: 52px; }
  .pred-img.dog { background: #EAF3DE; }
  .pred-img.cat { background: #E6F1FB; }
  .pred-body { padding: 10px 12px; }
  .pred-badge { display: inline-block; font-size: 11px; font-weight: 500; padding: 3px 8px; border-radius: 100px; margin-bottom: 6px; }
  .pred-badge.dog { background: #C0DD97; color: #27500A; }
  .pred-badge.cat { background: #B5D4F4; color: #0C447C; }
  .pred-file { font-size: 12px; color: var(--color-text-secondary); font-family: var(--font-mono); margin-bottom: 8px; }
  .conf-label { font-size: 11px; color: var(--color-text-secondary); margin-bottom: 4px; display: flex; justify-content: space-between; }
  .conf-bar { height: 5px; background: var(--color-background-secondary); border-radius: 3px; overflow: hidden; }
  .conf-fill { height: 100%; border-radius: 3px; }
  .conf-fill.dog { background: #639922; }
  .conf-fill.cat { background: #378ADD; }

  .struct-list { background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); overflow: hidden; }
  .struct-item { display: flex; align-items: center; gap: 12px; padding: 10px 16px; border-bottom: 0.5px solid var(--color-border-tertiary); font-size: 13px; }
  .struct-item:last-child { border-bottom: none; }
  .struct-icon { font-size: 15px; flex-shrink: 0; width: 20px; text-align: center; }
  .struct-name { font-family: var(--font-mono); font-size: 12px; color: var(--color-text-primary); flex: 1; }
  .struct-desc { font-size: 12px; color: var(--color-text-secondary); }

  .install-block { background: #2C2C2A; border-radius: var(--border-radius-md); padding: 1rem 1.25rem; font-family: var(--font-mono); font-size: 13px; color: #B4B2A9; line-height: 2; }
  .cmd-prompt { color: #639922; }
  .cmd-text { color: #E1F5EE; }

  .future-list { display: flex; flex-direction: column; gap: 8px; }
  .future-item { display: flex; align-items: center; gap: 10px; font-size: 14px; color: var(--color-text-secondary); padding: 10px 14px; background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-md); }
  .future-dot { width: 8px; height: 8px; border-radius: 50%; flex-shrink: 0; }
  .dot-purple { background: #7F77DD; }
  .dot-teal { background: #1D9E75; }
  .dot-amber { background: #EF9F27; }
  .dot-blue { background: #378ADD; }

  .ack-row { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 0.5rem; }
  .ack-pill { font-size: 13px; color: var(--color-text-secondary); background: var(--color-background-secondary); padding: 6px 14px; border-radius: 100px; border: 0.5px solid var(--color-border-tertiary); }
</style>

<div class="readme">

  <div class="hero">
    <span class="hero-emoji">🐶🐱</span>
    <h1>Dog vs Cat Breed Classifier</h1>
    <p>A deep learning–based image classification project that distinguishes between dogs and cats using TensorFlow and MobileNetV2. The model is trained on a Kaggle dataset and deployed with a simple Streamlit web app for real-time interaction.</p>
    <div class="tags">
      <span class="tag tag-green">TensorFlow</span>
      <span class="tag tag-blue">MobileNetV2</span>
      <span class="tag tag-amber">Streamlit</span>
      <span class="tag tag-purple">Transfer Learning</span>
      <span class="tag tag-green">Kaggle Dataset</span>
    </div>
  </div>

  <div class="stats-grid">
    <div class="stat-card">
      <div class="stat-label">Input Size</div>
      <div class="stat-value">224²</div>
      <div class="stat-sub">px × px</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Classes</div>
      <div class="stat-value">104</div>
      <div class="stat-sub">Dogs + Cats</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Top Confidence</div>
      <div class="stat-value">83%</div>
      <div class="stat-sub">on test images</div>
    </div>
    <div class="stat-card">
      <div class="stat-label">Architecture</div>
      <div class="stat-value" style="font-size:14px; padding-top: 4px;">MobileNetV2</div>
      <div class="stat-sub">pretrained</div>
    </div>
  </div>

  <div class="section">
    <div class="section-title"><span>✦</span> Features</div>
    <div class="feature-grid">
      <div class="feature-card"><div class="feature-icon">🔍</div><div class="feature-text"><strong>Image Classification</strong>Identifies dogs and cats from any uploaded image</div></div>
      <div class="feature-card"><div class="feature-icon">⚡</div><div class="feature-text"><strong>Transfer Learning</strong>Leverages pretrained MobileNetV2 weights for fast, accurate results</div></div>
      <div class="feature-card"><div class="feature-icon">🌐</div><div class="feature-text"><strong>Interactive Streamlit UI</strong>Simple web interface — no code required to use</div></div>
      <div class="feature-card"><div class="feature-icon">📊</div><div class="feature-text"><strong>Confidence Scores</strong>Returns a probability score alongside every prediction</div></div>
    </div>
  </div>

  <div class="section">
    <div class="section-title"><span>🧠</span> Model Details</div>
    <div class="arch-card">
      <div class="arch-row"><span class="key">Architecture</span><span class="val">MobileNetV2</span></div>
      <div class="arch-row"><span class="key">Framework</span><span class="val">TensorFlow / Keras</span></div>
      <div class="arch-row"><span class="key">Dataset</span><span class="val">Kaggle — Dogs and Cats Breed Classifier</span></div>
      <div class="arch-row"><span class="key">Input shape</span><span class="val">224 × 224 × 3</span></div>
      <div class="arch-row"><span class="key">Output</span><span class="val">Multi-Class classification (softmax)</span></div>
      <div class="arch-row"><span class="key">Saved format</span><span class="val">.keras (latest_model.keras)</span></div>
    </div>
  </div>
  <div class="section">
    <div class="section-title"><span>🏷️</span> Supported Breeds</div>
    <div class="arch-card">
      <p style="font-size: 13px; color: var(--color-text-secondary); margin-bottom: 1rem;">
        The model is trained to recognize a wide variety of specific breeds across two main categories.
      </p>
      <details style="cursor: pointer; margin-bottom: 0.75rem;">
        <summary style="font-size: 14px; font-weight: 500; color: var(--color-text-primary); padding: 8px 0;">
          🐱 View Cat Breeds (14)
        </summary>
        <div style="font-size: 13px; color: var(--color-text-secondary); padding: 10px; line-height: 1.6; background: var(--color-background-secondary); border-radius: 8px;">
          Abyssinian, American Shorthair, Bengal, Birman, Bombay, British Shorthair, Egyptian Mau, Maine Coon, Persian, Ragdoll, Russian Blue, Scottish Fold, Siamese, Sphynx.
        </div>
      </details>
      <details style="cursor: pointer;">
        <summary style="font-size: 14px; font-weight: 500; color: var(--color-text-primary); padding: 8px 0;">
          🐶 View Dog Breeds (90)
        </summary>
        <div style="font-size: 13px; color: var(--color-text-secondary); padding: 10px; line-height: 1.6; background: var(--color-background-secondary); border-radius: 8px;">
          <strong>A-C:</strong> Afghan, African Wild Dog, Airedale, Akita, American Hairless, American Spaniel, Aspin, Basenji, Basset, Beagle, Bearded Collie, Bernese Mountain, Bichon Frise, Blenheim, Bloodhound, Bluetick, Border Collie, Borzoi, Boston Terrier, Boxer, Bull Mastiff, Bull Terrier, Bulldog, French Bulldog, Cairn, Cavalier King Charles Spaniel, Chihuahua, Chinese Crested, Chow, Clumber, Cockapoo, Cocker, Collie, Corgi, Coyote. <br><br>
          <strong>D-L:</strong> Dachshund, Dalmatian, Dhole, Dingo, Doberman Pinscher, Elk Hound, Flat-Coated Retriever, German Shepherd, Golden Retriever, Great Dane, Great Pyrenees, Greyhound, Groenendael, Havanese, Irish Spaniel, Irish Wolfhound, Japanese Spaniel, Komondor, Labradoodle, Labrador Retriever, Lhasa. <br><br>
          <strong>M-Z:</strong> Malinois, Maltese, Mexican Hairless, Miniature Schnauzer, Newfoundland, Pekinese, Pit Bull, Pomeranian, Poodle, Pug, Rhodesian, Rottweiler, Saint Bernard, Schnauzer, Scotch Terrier, Shar Pei, Shetland Sheepdog, Shiba Inu, Shih-Tzu, Siberian Husky, Vizsla, Yorkie.
        </div>
      </details>
    </div>
  </div>  
  <div class="section">
    <div class="section-title"><span>🧪</span> Sample Predictions</div>
    <div class="predictions">
      <div class="pred-card">
        <div class="pred-img dog"><img src='./test_images/dog1.jpg'></div>
        <div class="pred-body">
          <span class="pred-badge dog">Dog-Boxer</span>
          <div class="pred-file">test_images/dog1.jpg</div>
          <div class="conf-label"><span>Confidence</span><span>97%</span></div>
          <div class="conf-bar"><div class="conf-fill dog" style="width:97%"></div></div>
        </div>
      </div>
      <div class="pred-card">
        <div class="pred-img cat"><img src='./test_images/cat1.jpg'></div>
        <div class="pred-body">
          <span class="pred-badge cat">Cat-Bengal</span>
          <div class="pred-file">test_images/cat1.jpg</div>
          <div class="conf-label"><span>Confidence</span><span>99%</span></div>
          <div class="conf-bar"><div class="conf-fill cat" style="width:95%"></div></div>
        </div>
      </div>
      <div class="pred-card">
        <div class="pred-img dog"><img src='./test_images/dog2.jpg'></div>
        <div class="pred-body">
          <span class="pred-badge dog">Dog-Pitbull</span>
          <div class="pred-file">test_images/dog2.jpg</div>
          <div class="conf-label"><span>Confidence</span><span>92%</span></div>
          <div class="conf-bar"><div class="conf-fill dog" style="width:92%"></div></div>
        </div>
      </div>
    </div>
  </div>

  <div class="section">
    <div class="section-title"><span>📂</span> Project Structure</div>
    <div class="struct-list">
      <div class="struct-item"><div class="struct-icon">🐍</div><div class="struct-name">app.py</div><div class="struct-desc">Streamlit web app</div></div>
      <div class="struct-item"><div class="struct-icon">📓</div><div class="struct-name">animal-classify.ipynb</div><div class="struct-desc">Model training notebook</div></div>
      <div class="struct-item"><div class="struct-icon">💾</div><div class="struct-name">latest_model.keras</div><div class="struct-desc">Trained model file</div></div>
      <div class="struct-item"><div class="struct-icon">🖼</div><div class="struct-name">test_images/</div><div class="struct-desc">Sample images for demo</div></div>
      <div class="struct-item"><div class="struct-icon">📄</div><div class="struct-name">README.md</div><div class="struct-desc">Project documentation</div></div>
    </div>
  </div>

  <div class="section">
    <div class="section-title"><span>⚙️</span> Installation</div>
    <div class="install-block">
      <div><span class="cmd-prompt">$</span> <span class="cmd-text">git clone https://github.com/imperiorhackers9934/dog-cat-classifier.git</span></div>
      <div><span class="cmd-prompt">$</span> <span class="cmd-text">cd dog-cat-classifier</span></div>
      <div><span class="cmd-prompt">$</span> <span class="cmd-text">pip install -r requirements.txt</span></div>
      <div><span class="cmd-prompt">$</span> <span class="cmd-text">streamlit run app.py</span></div>
    </div>
  </div>

  <div class="section">
    <div class="section-title"><span>🔮</span> Future Improvements</div>
    <div class="future-list">
      <div class="future-item"><div class="future-dot dot-purple"></div>Multi-breed classification support</div>
      <div class="future-item"><div class="future-dot dot-teal"></div>Mobile app deployment</div>
      <div class="future-item"><div class="future-dot dot-amber"></div>Model optimization with TensorFlow Lite</div>
      <div class="future-item"><div class="future-dot dot-blue"></div>Better accuracy with more training and testing data</div>
    </div>
  </div>

  <div class="section">
    <div class="section-title"><span>🙌</span> Acknowledgements</div>
    <div class="ack-row">
      <span class="ack-pill">TensorFlow & Keras</span>
      <span class="ack-pill">Kaggle Dataset Contributors</span>
      <span class="ack-pill">Streamlit</span>
      <span class="ack-pill">MIT License</span>
    </div>
  </div>

</div>
