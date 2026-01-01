from crew import LatestAiDevelopmentCrew

def run():
    inputs = {
        'topic': 'AI Agents'
    }
    LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
