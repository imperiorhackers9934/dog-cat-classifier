import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# Load model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model(
        "latest_model.keras",
        compile=False,
        safe_mode=False
    )
    return model

model = load_model()
class_names=['cat - abyssinian','cat - american shorthair','cat - bengal','cat - birman','cat - bombay','cat - british shorthair','cat - egyptian mau','cat - maine coon','cat - mainecoon','cat - persian','cat - ragdoll','cat - russian blue','cat - scottishfold','cat - siamese','cat - sphinx','cat - sphynx','dog - afghan','dog - african wild dog','dog - airedale','dog - akita','dog - american hairless','dog - american spaniel','dog - aspin','dog - basenji','dog - basset','dog - beagle','dog - bearded collie','dog - bermaise','dog - bernard-dog - saint','dog - bernese mountain','dog - bichon frise','dog - blenheim','dog - bloodhound','dog - bluetick','dog - border collie','dog - border-dog - collie','dog - borzoi','dog - boston terrier','dog - boxer','dog - bull mastiff','dog - bull terrier','dog - bulldog','dog - bulldong-dog - french','dog - cairn','dog - cavalier-dog - charles-dog - king-dog - spaniel','dog - chihuahua','dog - chinese crested','dog - chow','dog - clumber','dog - coated-dog - flat-dog - retriever','dog - cockapoo','dog - cocker','dog - collie','dog - corgi','dog - coyote','dog - dachshund','dog - dalmatian','dog - dhole','dog - dingo','dog - doberman','dog - doberman-dog - pinscher','dog - elk hound','dog - french bulldog','dog - german sheperd','dog - german-dog - sheperd','dog - golden retriever','dog - golden-dog - retriever','dog - great dane','dog - great perenees','dog - greyhound','dog - groenendael','dog - havanese','dog - husky-dog - siberian','dog - irish spaniel','dog - irish wolfhound','dog - japanese spaniel','dog - komondor','dog - labradoodle','dog - labrador','dog - labrador-dog - retriever','dog - lhasa','dog - malinois','dog - maltese','dog - mex hairless','dog - miniature-dog - schnauzer','dog - newfoundland','dog - pekinese','dog - pit bull','dog - pomeranian','dog - poodle','dog - pug','dog - rhodesian','dog - rottweiler','dog - saint bernard','dog - schnauzer','dog - scotch terrier','dog - shar pei','dog - sheepdog-dog - shetland','dog - shiba inu','dog - shih-dog - tzu','dog - shih-tzu','dog - siberian husky','dog - vizsla','dog - yorkie']
st.title("🖼️ Dog / Cat Classification App")
st.write("Upload your pet's image and get breed predictions from our trained model.")

# File uploader
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

def preprocess_image(image):
    # Resize directly (PIL supports this)
    image = image.resize((224, 224))
    
    # Convert to array
    img_array = np.array(image)
    
    # Expand dims
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    
    st.image(image, caption="Uploaded Image", width="stretch")
    
    processed_image = preprocess_image(image)
    
    if st.button("Predict"):
        prediction = model.predict(processed_image)
        
        st.subheader("Prediction Output:")
        # Handle classification output
        class_index = np.argmax(prediction)
        preds = prediction[0]
        top_indices = np.argsort(preds)[-5:][::-1]
        st.success(f"Predicted Class : {class_names[class_index]}")
        st.subheader("Top Results:")
        for i in top_indices:
            st.write(f"{class_names[i]}: {preds[i]:.2f}")