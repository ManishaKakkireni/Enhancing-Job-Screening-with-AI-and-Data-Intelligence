import jd_summarizer
import cv_parser
import matching_engine
import shortlisting
import interview_scheduler

# Sample JD and CV
jd_text = "Looking for a Python Developer with experience in NLP and Machine Learning."
cv_text = "Experienced in Python, NLP, and ML. Worked on AI projects."

print("🔍 Summarizing Job Description...")
jd_keywords = jd_summarizer.summarize_jd(jd_text)
print("JD Keywords:", jd_keywords)

print("\n🔍 Parsing Candidate CV...")
cv_keywords = cv_parser.parse_cv(cv_text)
print("CV Keywords:", cv_keywords)

print("\n🔍 Computing Match Score...")
match_score = matching_engine.compute_match_score(jd_keywords, cv_keywords)
print(f"Match Score: {match_score:.2f}%")

# Check if candidate is shortlisted
if match_score > 80:
    print("\n✅ Candidate Shortlisted!")
    shortlisting.store_candidate("John Doe", "johndoe@example.com", match_score)
    
    print("\n📩 Sending Interview Invitation Email...")
    interview_scheduler.send_email("johndoe@example.com", "Interview Invitation", 
                                   "You are shortlisted for an interview.")
else:
    print("\n❌ Candidate not shortlisted. Score too low.")
