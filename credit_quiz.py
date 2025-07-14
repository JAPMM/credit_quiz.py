import React, { useState, useEffect, useMemo } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Progress } from '@/components/ui/progress';
import { Badge } from '@/components/ui/badge';
import { CheckCircle, XCircle, RotateCcw, Trophy, BookOpen, TrendingUp, Star, Award } from 'lucide-react';

const QUESTIONS_CREDIT_BEGINNER = [
  {
    id: 1,
    type: "mcq",
    difficulty: "basic",
    topic: "payment_history",
    question: "Which action helps improve your credit score the most?",
    options: [
      "Paying bills on time",
      "Closing unused credit cards",
      "Applying for new credit often",
      "Carrying high balances"
    ],
    answer: "Paying bills on time",
    explanation: "Your payment history is the most important factor in your credit score, accounting for 35% of your FICO score.",
    resource: "https://www.myfico.com/credit-education/whats-in-your-credit-score"
  },
  {
    id: 2,
    type: "tf",
    difficulty: "basic",
    topic: "payment_history",
    question: "Paying late will hurt your credit score.",
    options: ["True", "False"],
    answer: "True",
    explanation: "Late payments have a major negative impact on your score and can stay on your report for up to 7 years.",
    resource: "https://www.experian.com/blogs/ask-experian/how-long-do-late-payments-stay-on-credit-report/"
  },
  {
    id: 3,
    type: "mcq",
    difficulty: "basic",
    topic: "credit_monitoring",
    question: "Which is a common credit myth?",
    options: [
      "Checking your own score hurts it",
      "Paying on time is important",
      "Low balances are best",
      "Don't max out your cards"
    ],
    answer: "Checking your own score hurts it",
    explanation: "Checking your own credit is a 'soft' inquiry and does not hurt your score. It's actually recommended to check regularly.",
    resource: "https://www.consumerfinance.gov/ask-cfpb/does-checking-my-credit-score-lower-it-en-314/"
  },
  {
    id: 4,
    type: "tf",
    difficulty: "intermediate",
    topic: "credit_repair",
    question: "Disputing errors on your credit report can improve your score.",
    options: ["True", "False"],
    answer: "True",
    explanation: "Removing inaccurate negative items through disputes can raise your score. You have the right to dispute errors under the Fair Credit Reporting Act.",
    resource: "https://www.ftc.gov/consumers/consumer-information/articles/0151-disputing-errors-credit-reports"
  },
  {
    id: 5,
    type: "mcq",
    difficulty: "intermediate",
    topic: "collections",
    question: "What should you do if you find a collection on your credit report?",
    options: [
      "Pay it off or dispute if wrong",
      "Ignore it",
      "Apply for new credit",
      "Close all credit accounts"
    ],
    answer: "Pay it off or dispute if wrong",
    explanation: "Paying collections or disputing inaccurate ones can prevent further damage. Consider negotiating a pay-for-delete agreement.",
    resource: "https://www.experian.com/blogs/ask-experian/how-to-remove-collections-from-credit-report/"
  },
  {
    id: 6,
    type: "tf",
    difficulty: "intermediate",
    topic: "new_credit",
    question: "Opening many new credit cards in a short time can lower your score.",
    options: ["True", "False"],
    answer: "True",
    explanation: "Many new accounts in a short time looks risky to lenders and can lower your score due to hard inquiries and reduced average account age.",
    resource: "https://www.creditkarma.com/credit-cards/i/how-many-credit-cards-should-i-have"
  },
  {
    id: 7,
    type: "mcq",
    difficulty: "basic",
    topic: "payment_history",
    question: "Which factor has the biggest impact on your credit score?",
    options: [
      "Payment history",
      "Credit mix",
      "Length of credit history",
      "Number of accounts"
    ],
    answer: "Payment history",
    explanation: "On-time payments make up 35% of your FICO credit score, making it the most important factor.",
    resource: "https://www.myfico.com/credit-education/whats-in-your-credit-score"
  },
  {
    id: 8,
    type: "mcq",
    difficulty: "basic",
    topic: "credit_building",
    question: "What is a good way to build credit?",
    options: [
      "Pay bills on time",
      "Max out credit cards",
      "Miss payments",
      "Avoid all credit"
    ],
    answer: "Pay bills on time",
    explanation: "Consistently paying bills on time is the foundation of good credit. Even one 30-day late payment can significantly impact your score.",
    resource: "https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/credit-reports-and-scores-basics/"
  },
  {
    id: 9,
    type: "tf",
    difficulty: "intermediate",
    topic: "credit_mix",
    question: "Having a mix of credit types (cards, loans) can help your score.",
    options: ["True", "False"],
    answer: "True",
    explanation: "Credit mix accounts for 10% of your FICO score. Having different types like credit cards, auto loans, and mortgages shows you can handle various credit responsibilities.",
    resource: "https://www.experian.com/blogs/ask-experian/what-is-credit-mix/"
  },
  {
    id: 10,
    type: "mcq",
    difficulty: "basic",
    topic: "payment_history",
    question: "Which should you avoid to keep a healthy credit score?",
    options: [
      "Missing payments",
      "Paying on time",
      "Keeping balances low",
      "Checking your own report"
    ],
    answer: "Missing payments",
    explanation: "Missing payments is the #1 credit killer. Even one missed payment can drop your score by 60-110 points.",
    resource: "https://www.myfico.com/credit-education/articles/late-payments-impact-credit-scores"
  },
  {
    id: 11,
    type: "tf",
    difficulty: "basic",
    topic: "credit_monitoring",
    question: "You should check your credit report every year.",
    options: ["True", "False"],
    answer: "True",
    explanation: "You're entitled to one free credit report annually from each bureau at AnnualCreditReport.com. Regular monitoring helps catch errors and fraud.",
    resource: "https://www.annualcreditreport.com"
  },
  {
    id: 12,
    type: "mcq",
    difficulty: "intermediate",
    topic: "credit_repair",
    question: "How long do most negative marks stay on your credit report?",
    options: [
      "7 years",
      "1 year",
      "3 years",
      "10 months"
    ],
    answer: "7 years",
    explanation: "Most negative items like late payments, collections, and charge-offs remain on your credit report for 7 years from the date of first delinquency.",
    resource: "https://www.experian.com/blogs/ask-experian/how-long-does-negative-information-stay-on-credit-report/"
  },
  {
    id: 13,
    type: "mcq",
    difficulty: "basic",
    topic: "credit_scores",
    question: "What does a credit score of 800+ mean?",
    options: [
      "Excellent credit",
      "Poor credit",
      "No credit history",
      "Too many inquiries"
    ],
    answer: "Excellent credit",
    explanation: "Scores above 800 are considered excellent by all lenders and qualify you for the best interest rates and terms.",
    resource: "https://www.experian.com/blogs/ask-experian/what-is-a-good-credit-score/"
  },
  {
    id: 14,
    type: "tf",
    difficulty: "intermediate",
    topic: "credit_utilization",
    question: "Maxing out your credit cards can lower your score.",
    options: ["True", "False"],
    answer: "True",
    explanation: "High credit utilization (using most of your available credit) makes you look risky to lenders and can significantly lower your score.",
    resource: "https://www.creditkarma.com/credit-cards/i/credit-utilization-and-your-credit-score"
  },
  {
    id: 15,
    type: "mcq",
    difficulty: "intermediate",
    topic: "credit_building",
    question: "Which credit behavior is best?",
    options: [
      "Keep old cards open and pay on time",
      "Open and close cards often",
      "Only pay minimum payments",
      "Never use credit"
    ],
    answer: "Keep old cards open and pay on time",
    explanation: "Long credit history with consistent on-time payments is ideal. Closing old cards can hurt your credit utilization ratio and average account age.",
    resource: "https://www.nerdwallet.com/article/credit-cards/should-you-close-a-credit-card"
  },
  {
    id: 16,
    type: "mcq",
    difficulty: "intermediate",
    topic: "credit_repair",
    question: "Which can help fix errors on your credit report?",
    options: [
      "File a dispute",
      "Ignore it",
      "Close all credit cards",
      "Increase balances"
    ],
    answer: "File a dispute",
    explanation: "Filing a dispute with the credit bureau is your right under the Fair Credit Reporting Act. They must investigate within 30 days.",
    resource: "https://www.ftc.gov/consumers/consumer-information/articles/0151-disputing-errors-credit-reports"
  },
  {
    id: 17,
    type: "tf",
    difficulty: "basic",
    topic: "credit_monitoring",
    question: "You can get a free credit report every year.",
    options: ["True", "False"],
    answer: "True",
    explanation: "AnnualCreditReport.com is the only authorized source for free annual credit reports from all three major credit bureaus.",
    resource: "https://www.annualcreditreport.com"
  },
  {
    id: 18,
    type: "mcq",
    difficulty: "intermediate",
    topic: "credit_building",
    question: "Which is NOT a good way to build credit?",
    options: [
      "Making payments on time",
      "Opening many accounts quickly",
      "Keeping balances low",
      "Checking your report"
    ],
    answer: "Opening many accounts quickly",
    explanation: "Opening too many accounts quickly can lower your score due to hard inquiries and make you appear desperate for credit to lenders.",
    resource: "https://www.experian.com/blogs/ask-experian/how-many-credit-cards-should-you-have/"
  },
  {
    id: 19,
    type: "mcq",
    difficulty: "advanced",
    topic: "credit_building",
    question: "What does it mean if you are a co-signer?",
    options: [
      "You share responsibility for the loan",
      "You own the loan alone",
      "You have no responsibility",
      "You can't build credit"
    ],
    answer: "You share responsibility for the loan",
    explanation: "A co-signer is equally responsible for loan repayment. If the primary borrower defaults, you're liable for the full debt.",
    resource: "https://www.consumerfinance.gov/ask-cfpb/what-should-i-know-about-being-a-cosigner-on-someones-loan-en-1369/"
  },
  {
    id: 20,
    type: "tf",
    difficulty: "intermediate",
    topic: "alternative_credit",
    question: "Paying rent on time can help your credit score if reported.",
    options: ["True", "False"],
    answer: "True",
    explanation: "Some rental reporting services and landlords report rent payments to credit bureaus, which can help build credit history.",
    resource: "https://www.experian.com/blogs/ask-experian/can-paying-rent-help-your-credit-score/"
  }
];

const DIFFICULTY_COLORS = {
  basic: "bg-green-100 text-green-800",
  intermediate: "bg-yellow-100 text-yellow-800",
  advanced: "bg-red-100 text-red-800"
};

const TOPIC_LABELS = {
  payment_history: "Payment History",
  credit_utilization: "Credit Utilization",
  credit_monitoring: "Credit Monitoring",
  credit_repair: "Credit Repair",
  collections: "Collections",
  new_credit: "New Credit",
  credit_mix: "Credit Mix",
  credit_building: "Credit Building",
  credit_scores: "Credit Scores",
  alternative_credit: "Alternative Credit"
};

const CreditQuizApp = () => {
  const [currentQuiz, setCurrentQuiz] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const [showResults, setShowResults] = useState(false);
  const [quizHistory, setQuizHistory] = useState([]);
  const [selectedDifficulty, setSelectedDifficulty] = useState('all');
  const [selectedTopic, setSelectedTopic] = useState('all');
  const [showCertificate, setShowCertificate] = useState(false);

  // Initialize quiz
  const initializeQuiz = () => {
    let filteredQuestions = QUESTIONS_CREDIT_BEGINNER;
    
    if (selectedDifficulty !== 'all') {
      filteredQuestions = filteredQuestions.filter(q => q.difficulty === selectedDifficulty);
    }
    
    if (selectedTopic !== 'all') {
      filteredQuestions = filteredQuestions.filter(q => q.topic === selectedTopic);
    }
    
    const shuffled = [...filteredQuestions].sort(() => Math.random() - 0.5);
    const selected = shuffled.slice(0, Math.min(10, shuffled.length));
    
    setCurrentQuiz(selected);
    setCurrentQuestion(0);
    setAnswers({});
    setShowResults(false);
    setShowCertificate(false);
  };

  // Initialize quiz on component mount
  useEffect(() => {
    initializeQuiz();
  }, [selectedDifficulty, selectedTopic]);

  // Calculate progress
  const progress = ((currentQuestion + 1) / currentQuiz.length) * 100;

  // Handle answer selection
  const handleAnswer = (questionId, answer) => {
    setAnswers(prev => ({
      ...prev,
      [questionId]: answer
    }));
  };

  // Navigate to next question
  const nextQuestion = () => {
    if (currentQuestion < currentQuiz.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
    }
  };

  // Navigate to previous question
  const prevQuestion = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  };

  // Submit quiz
  const submitQuiz = () => {
    const score = currentQuiz.reduce((acc, question) => {
      return acc + (answers[question.id] === question.answer ? 1 : 0);
    }, 0);
    
    const percentage = (score / currentQuiz.length) * 100;
    
    const quizResult = {
      date: new Date().toISOString(),
      score,
      total: currentQuiz.length,
      percentage,
      difficulty: selectedDifficulty,
      topic: selectedTopic,
      questions: currentQuiz.map(q => ({
        id: q.id,
        topic: q.topic,
        difficulty: q.difficulty,
        correct: answers[q.id] === q.answer
      }))
    };
    
    setQuizHistory(prev => [...prev, quizResult]);
    setShowResults(true);
    
    // Show certificate for high scores
    if (percentage >= 80) {
      setShowCertificate(true);
    }
  };

  // Get personalized recommendations
  const getRecommendations = () => {
    if (!showResults || quizHistory.length === 0) return [];
    
    const lastQuiz = quizHistory[quizHistory.length - 1];
    const weakTopics = lastQuiz.questions
      .filter(q => !q.correct)
      .reduce((acc, q) => {
        acc[q.topic] = (acc[q.topic] || 0) + 1;
        return acc;
      }, {});
    
    const recommendations = Object.entries(weakTopics)
      .sort(([,a], [,b]) => b - a)
      .slice(0, 3)
      .map(([topic]) => ({
        topic,
        label: TOPIC_LABELS[topic],
        suggestion: getTopicSuggestion(topic)
      }));
    
    return recommendations;
  };

  const getTopicSuggestion = (topic) => {
    const suggestions = {
      payment_history: "Focus on setting up automatic payments and payment reminders",
      credit_utilization: "Work on paying down balances and keeping utilization below 30%",
      credit_monitoring: "Set up regular credit monitoring and annual report reviews",
      credit_repair: "Learn about dispute processes and credit repair strategies",
      collections: "Understand how to handle collections and negotiate settlements",
      new_credit: "Learn about the impact of new credit applications and inquiries",
      credit_mix: "Understand how different types of credit affect your score",
      credit_building: "Focus on building a strong credit foundation with secured cards",
      credit_scores: "Learn about different scoring models and what affects your score",
      alternative_credit: "Explore alternative ways to build credit like rent reporting"
    };
    return suggestions[topic] || "Continue learning about this topic";
  };

  // Get difficulty distribution
  const difficulties = ['basic', 'intermediate', 'advanced'];
  const topics = [...new Set(QUESTIONS_CREDIT_BEGINNER.map(q => q.topic))];

  if (currentQuiz.length === 0) {
    return (
      <div className="max-w-4xl mx-auto p-6">
        <Card>
          <CardContent className="p-8 text-center">
            <BookOpen className="w-16 h-16 mx-auto mb-4 text-blue-500" />
            <h2 className="text-2xl font-bold mb-4">No Questions Available</h2>
            <p className="text-gray-600 mb-4">
              No questions match your current filters. Try adjusting your difficulty or topic selection.
            </p>
            <Button onClick={() => {
              setSelectedDifficulty('all');
              setSelectedTopic('all');
            }}>
              Reset Filters
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  if (showResults) {
    const lastQuiz = quizHistory[quizHistory.length - 1];
    const recommendations = getRecommendations();
    
    return (
      <div className="max-w-4xl mx-auto p-6 space-y-6">
        {/* Certificate Modal */}
        {showCertificate && (
          <Card className="border-gold border-2 bg-gradient-to-br from-yellow-50 to-yellow-100">
            <CardContent className="p-8 text-center">
              <Award className="w-16 h-16 mx-auto mb-4 text-yellow-600" />
              <h2 className="text-3xl font-bold text-yellow-800 mb-2">🎉 Congratulations! 🎉</h2>
              <p className="text-lg text-yellow-700 mb-4">
                You've earned a Certificate of Excellence!
              </p>
              <div className="bg-white p-4 rounded-lg shadow-md">
                <p className="text-xl font-semibold">Credit Education Certificate</p>
                <p className="text-gray-600">Score: {lastQuiz.percentage}%</p>
                <p className="text-gray-600">Date: {new Date(lastQuiz.date).toLocaleDateString()}</p>
              </div>
            </CardContent>
          </Card>
        )}

        {/* Results Summary */}
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Trophy className="w-6 h-6" />
              Quiz Results
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
              <div className="text-center">
                <div className="text-3xl font-bold text-blue-600">{lastQuiz.score}</div>
                <div className="text-gray-600">Correct Answers</div>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold text-green-600">{lastQuiz.percentage}%</div>
                <div className="text-gray-600">Score</div>
              </div>
              <div className="text-center">
                <div className="text-3xl font-bold text-purple-600">{lastQuiz.total}</div>
                <div className="text-gray-600">Total Questions</div>
              </div>
            </div>
            
            <div className="mb-6">
              <div className="flex justify-between items-center mb-2">
                <span className="text-sm text-gray-600">Performance</span>
                <span className="text-sm text-gray-600">{lastQuiz.percentage}%</span>
              </div>
              <Progress value={lastQuiz.percentage} className="h-3" />
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <h4 className="font-semibold mb-2">Quiz Details</h4>
                <p className="text-sm text-gray-600">Difficulty: {selectedDifficulty}</p>
                <p className="text-sm text-gray-600">Topic: {selectedTopic === 'all' ? 'All Topics' : TOPIC_LABELS[selectedTopic]}</p>
                <p className="text-sm text-gray-600">Date: {new Date(lastQuiz.date).toLocaleDateString()}</p>
              </div>
              <div>
                <h4 className="font-semibold mb-2">Performance Level</h4>
                <Badge className={
                  lastQuiz.percentage >= 80 ? "bg-green-100 text-green-800" :
                  lastQuiz.percentage >= 60 ? "bg-yellow-100 text-yellow-800" :
                  "bg-red-100 text-red-800"
                }>
                  {lastQuiz.percentage >= 80 ? "Excellent" : 
                   lastQuiz.percentage >= 60 ? "Good" : "Needs Improvement"}
                </Badge>
              </div>
            </div>
          </CardContent>
        </Card>

        {/* Question Review */}
        <Card>
          <CardHeader>
            <CardTitle>Question Review</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4">
              {currentQuiz.map((question, index) => {
                const userAnswer = answers[question.id];
                const isCorrect = userAnswer === question.answer;
                
                return (
                  <div key={question.id} className="border rounded-lg p-4">
                    <div className="flex items-start gap-3">
                      <div className="flex-shrink-0 mt-1">
                        {isCorrect ? 
                          <CheckCircle className="w-5 h-5 text-green-500" /> : 
                          <XCircle className="w-5 h-5 text-red-500" />
                        }
                      </div>
                      <div className="flex-1">
                        <div className="flex items-center gap-2 mb-2">
                          <span className="font-semibold">Q{index + 1}:</span>
                          <Badge className={DIFFICULTY_COLORS[question.difficulty]}>
                            {question.difficulty}
                          </Badge>
                          <Badge variant="outline">
                            {TOPIC_LABELS[question.topic]}
                          </Badge>
                        </div>
                        <p className="mb-2">{question.question}</p>
                        <div className="text-sm space-y-1">
                          <p>
                            <span className="text-gray-600">Your answer:</span> 
                            <span className={isCorrect ? "text-green-600 font-medium" : "text-red-600 font-medium"}>
                              {userAnswer}
                            </span>
                          </p>
                          {!isCorrect && (
                            <p>
                              <span className="text-gray-600">Correct answer:</span> 
                              <span className="text-green-600 font-medium">{question.answer}</span>
                            </p>
                          )}
                          <p className="text-gray-600 bg-gray-50 p-2 rounded">
                            <strong>Explanation:</strong> {question.explanation}
                          </p>
                          {question.resource && (
                            <p className="text-sm">
                              <a href={question.resource} target="_blank" rel="noopener noreferrer" 
                                 className="text-blue-600 hover:underline">
                                📚 Learn More
                              </a>
                            </p>
                          )}
                        </div>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          </CardContent>
        </Card>

        {/* Personalized Recommendations */}
        {recommendations.length > 0 && (
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <TrendingUp className="w-6 h-6" />
                Personalized Recommendations
              </CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                {recommendations.map((rec, index) => (
                  <div key={index} className="border rounded-lg p-4">
                    <h4 className="font-semibold mb-2">{rec.label}</h4>
                    <p className="text-sm text-gray-600">{rec.suggestion}</p>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        )}

        {/* Quiz History */}
        {quizHistory.length > 1 && (
          <Card>
            <CardHeader>
              <CardTitle>Progress History</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="space-y-2">
                {quizHistory.slice(-5).map((quiz, index) => (
                  <div key={index} className="flex items-center justify-between p-3 bg-gray-50 rounded">
                    <div>
                      <span className="font-medium">{quiz.score}/{quiz.total}</span>
                      <span className="text-gray-600 ml-2">
                        ({quiz.percentage}%) - {new Date(quiz.date).toLocaleDateString()}
                      </span>
                    </div>
                    <Badge className={
                      quiz.percentage >= 80 ? "bg-green-100 text-green-800" :
                      quiz.percentage >= 60 ? "bg-yellow-100 text-yellow-800" :
                      "bg-red-100 text-red-800"
                    }>
                      {quiz.percentage >= 80 ? "Excellent" : 
                       quiz.percentage >= 60 ? "Good" : "Needs Work"}
                    </Badge>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>
        )}

        {/* Action Buttons */}
        <div className="flex gap-4 justify-center">
          <Button onClick={initializeQuiz} className="flex items-center gap-2">
            <RotateCcw className="w-4 h-4" />
            Take Another Quiz
          </Button>
        </div>
      </div>
    );
  }

  // Quiz interface
  const question = currentQuiz[currentQuestion];
  const hasAnswered = answers[question.id] !== undefined;

  return (
    <div className="max-w-4xl mx-auto p-6">
      {/* Header */}
      <div className="text-center mb-8">
        <h1 className="text-3xl font-bold mb-4">💳 Credit Education Quiz</h1>
        <div className="flex flex-wrap justify-center gap-4 mb-4">
          <div>
            <label className="block text-sm font-medium mb-1">Difficulty</label>
            <select 
              value={selectedDifficulty} 
              onChange={(e) => setSelectedDifficulty(e.target.value)}
              className="px-3 py-2 border rounded-lg"
            >
              <option value="all">All Levels</option>
              <option value="basic">Basic</option>
              <option value="intermediate">Intermediate</option>
              <option value="advanced">Advanced</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium mb-1">Topic</label>
            <select 
              value={selectedTopic} 
              onChange={(e) => setSelectedTopic(e.target.value)}
              className="px-3 py-2 border rounded-lg"
            >
              <option value="all">All Topics</option>
              {topics.map(topic => (
                <option key={topic} value={topic}>{TOPIC_LABELS[topic]}</option>
              ))}
            </select>
          </div>
        </div>
      </div>

      {/* Progress Bar */}
      <div className="mb-6">
        <div className="flex justify-between items-center mb-2">
          <span className="text-sm font-medium">
            Question {currentQuestion + 1} of {currentQuiz.length}
          </span>
          <span className="text-sm text-gray-600">{Math.round(progress)}% Complete</span>
        </div>
        <Progress value={progress} className="h-3" />
      </div>

      {/* Question Card */}
      <Card className="mb-6">
        <CardHeader>
          <div className="flex items-center gap-2 mb-2">
            <Badge className={DIFFICULTY_COLORS[question.difficulty]}>
              {question.difficulty}
            </Badge>
            <Badge variant="outline">
              {TOPIC_LABELS[question.topic]}
            </Badge>
          </div>
          <CardTitle className="text-lg">
            {question.question}
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-3">
            {question.options.map((option, index) => (
              <button
                key={index}
                onClick={() => handleAnswer(question.id, option)}
                className={`w-full p-4 text-left rounded-lg border transition-colors ${
                  answers[question.id] === option
                    ? 'bg-blue-50 border-blue-500 text-blue-700'
                    : 'bg-white border-gray-200 hover:bg-gray-50'
                }`}
              >
                {option}
              </button>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Navigation */}
      <div className="flex justify-between items-center">
        <Button 
          onClick={prevQuestion} 
          disabled={currentQuestion === 0}
          variant="outline"
        >
          Previous
        </Button>
        
        <div className="flex gap-2">
          {currentQuiz.map((_, index) => (
            <button
              key={index}
              onClick={() => setCurrentQuestion(index)}
              className={`w-8 h-8 rounded-full text-sm font-medium transition-colors ${
                index === currentQuestion
                  ? 'bg-blue-500 text-white'
                  : answers[currentQuiz[index].id]
                  ? 'bg-green-500 text-white'
                  : 'bg-gray-200 text-gray-600 hover:bg-gray-300'
              }`}
            >
              {index + 1}
            </button>
          ))}
        </div>

        {currentQuestion === currentQuiz.length - 1 ? (
          <Button 
            onClick={submitQuiz}
            disabled={Object.keys(answers).length < currentQuiz.length}
            className="bg-green-600 hover:bg-green-700"
          >
            Submit Quiz
          </Button>
        ) : (
          <Button 
            onClick={nextQuestion}
            disabled={!hasAnswered}
          >
            Next
          </Button>
        )}
      </div>

      {/* Answer Status */}
      <div className="mt-4 text-center">
        <p className="text-sm text-gray-600">
          Answered: {Object.keys(answers).length} of {currentQuiz.length} questions
        </p>
      </div>
    </div>
  );
};

export default CreditQuizApp;
