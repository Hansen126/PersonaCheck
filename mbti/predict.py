import pandas as pd
import glob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.decomposition import TruncatedSVD

# print test
print("line test")

all_files = glob.glob("mbti/MBTI500_part_*.csv")
data = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)

X = data['posts']
y = data['type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= 42)

def to_dense(X):
    return X.toarray()


pipeSVC = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')), 
    ('svd', TruncatedSVD(n_components=100)),  
    ('gnb', LinearSVC())  
])

pipeSVC.fit(X_train, y_train)

print("Model training complete")

def predict_mbti(text):
    print(f"Received text: {text}")
    result = pipeSVC.predict([text])
    print(f"Prediction result: {result}")
    return result[0]    

# test
sample_text = "I enjoy spending time alone, reading books, and analyzing situations deeply."
print("Making prediction...")
mbti_type = predict_mbti(sample_text)
print(f"The predicted MBTI type is: {mbti_type}")

# MBTI description
descISTJ = "Quiet, serious, earn success by being thorough and dependable. Practical, matter-of-fact, realistic, and responsible. Decide logically what should be done and work toward it steadily, regardless of distractions. Take pleasure in making everything orderly and organized—their work, their home, their life. Value traditions and loyalty."
descISFJ = "Quiet, friendly, responsible, and conscientious. Committed and steady in meeting their obligations. Thorough, painstaking, and accurate. Loyal, considerate, notice and remember specifics about people who are important to them, concerned with how others feel. Strive to create an orderly and harmonious environment at work and at home."
descINFJ = "Seek meaning and connection in ideas, relationships, and material possessions. Want to understand what motivates people and are insightful about others. Conscientious and committed to their firm values. Develop a clear vision about how best to serve the common good. Organized and decisive in implementing their vision."
descINTJ = "Have original minds and great drive for implementing their ideas and achieving their goals. Quickly see patterns in external events and develop long-range explanatory perspectives. When committed, organize a job and carry it through. Skeptical and independent, have high standards of competence and performance—for themselves and others."
descISTP = "Tolerant and flexible, quiet observers until a problem appears, then act quickly to find workable solutions. Analyze what makes things work and readily get through large amounts of data to isolate the core of practical problems. Interested in cause and effect, organize facts using logical principles, value efficiency."
descISFP = "Quiet, friendly, sensitive, and kind. Enjoy the present moment, what's going on around them. Like to have their own space and to work within their own time frame. Loyal and committed to their values and to people who are important to them. Dislike disagreements and conflicts; don't force their opinions or values on others."
descINFP = "Idealistic, loyal to their values and to people who are important to them. Want to live a life that is congruent with their values. Curious, quick to see possibilities, can be catalysts for implementing ideas. Seek to understand people and to help them fulfill their potential. Adaptable, flexible, and accepting unless a value is threatened."
descINTP = "Seek to develop logical explanations for everything that interests them. Theoretical and abstract, interested more in ideas than in social interaction. Quiet, contained, flexible, and adaptable. Have unusual ability to focus in depth to solve problems in their area of interest. Skeptical, sometimes critical, always analytical."
descESTP = "Flexible and tolerant, take a pragmatic approach focused on immediate results. Bored by theories and conceptual explanations; want to act energetically to solve the problem. Focus on the here and now, spontaneous, enjoy each moment they can be active with others. Enjoy material comforts and style. Learn best through doing."
descESFP = "Outgoing, friendly, and accepting. Exuberant lovers of life, people, and material comforts. Enjoy working with others to make things happen. Bring common sense and a realistic approach to their work and make work fun. Flexible and spontaneous, adapt readily to new people and environments. Learn best by trying a new skill with other people."
descENFP = "Warmly enthusiastic and imaginative. See life as full of possibilities. Make connections between events and information very quickly, and confidently proceed based on the patterns they see. Want a lot of affirmation from others, and readily give appreciation and support. Spontaneous and flexible, often rely on their ability to improvise and their verbal fluency."
descENTP = "Quick, ingenious, stimulating, alert, and outspoken. Resourceful in solving new and challenging problems. Adept at generating conceptual possibilities and then analyzing them strategically. Good at reading other people. Bored by routine, will seldom do the same thing the same way, apt to turn to one new interest after another."
descESTJ = "Practical, realistic, matter-of-fact. Decisive, quickly move to implement decisions. Organize projects and people to get things done, focus on getting results in the most efficient way possible. Take care of routine details. Have a clear set of logical standards, systematically follow them and want others to also. Forceful in implementing their plans." 
descESFJ = "Warmhearted, conscientious, and cooperative. Want harmony in their environment, work with determination to establish it. Like to work with others to complete tasks accurately and on time. Loyal, follow through even in small matters. Notice what others need in their day-to-day lives and try to provide it. Want to be appreciated for who they are and for what they contribute."
descENFJ = "Warm, empathetic, responsive, and responsible. Highly attuned to the emotions, needs, and motivations of others. Find potential in everyone, want to help others fulfill their potential. May act as catalysts for individual and group growth. Loyal, responsive to praise and criticism. Sociable, facilitate others in a group, and provide inspiring leadership."
descENTJ = "Frank, decisive, assume leadership readily. Quickly see illogical and inefficient procedures and policies, develop and implement comprehensive systems to solve organizational problems. Enjoy long-term planning and goal setting. Usually well informed, well read, enjoy expanding their knowledge and passing it on to others. Forceful in presenting their ideas."

def mbtiDescription(type):
    print(type)
    if type == "ISTJ":
        return descISTJ
    if type == "ISFJ":
        return descISFJ
    if type == "INFJ":
        return descINFJ
    if type == "INTJ":
        return descINTJ
    if type == "ISTP":
        return descISTP
    if type == "ISFP":
        return descISFJ
    if type == "INFP":
        return descINFP
    if type == "INTP":
        return descINTP
    if type == "ESTP":
        return descESTP
    if type == "ESFP":
        return descESFP
    if type == "ENFP":
        return descENFP
    if type == "ENTP":
        return descENTP
    if type == "ESTJ":
        return descESTJ
    if type == "ESFJ":
        return descESFJ
    if type == "ENFJ":
        return descENFJ
    if type == "ENTJ":
        return descENTJ
    return "MBTI description not found."