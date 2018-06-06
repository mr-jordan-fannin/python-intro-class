''' Population Estimator by Jordan Fannin. 5-22-2018'''


# Population class, constructor, and simulate method
class Population:
    # Population object constructor
    def __init__(self, data):
        self.start = data[0]['answer']
        self.rate = data[1]['answer']
        self.gestation = data[2]['answer']
        self.observation = data[3]['answer']

    # Runs simulation on object when called
    def simulate(self):
        total = self.start
        generations = int(self.observation / self.gestation)
        for generation in range(generations):
            total *= self.rate
            if total < 1:
                print(f"The organism went extinct after {generation} hour(s).")
                exit()
        try:
            print(f"Estimated population after {self.observation} hours "
                  f"at a growth rate of {self.rate} over {generations} generation(s): {int(total)}")
        except OverflowError:
            print("We're doomed!")


# Main function
def main():
    print('Population Growth Estimator')
    # List of dicts for user prompts, user responses, and error messages
    data = [
        {
            'question': 'Starting Population',
            'answer': 0,
            'error': 'The organism already went extinct.'
        },
        {
            'question': 'Growth Rate',
            'answer': 0,
            'error': 'That is not how this works.'
        },
        {
            'question': 'Gestation Period',
            'answer': 0,
            'error': 'Everything needs time to grow.'
        },
        {
            'question': 'Observation Period',
            'answer': 0,
            'error': 'You did not even bother to look.'
        }
    ]

    # Loop through questions and collect answers with error handling and give chance to re-enter answer if improper
    for i in data:
        while (True):
            # Gather starting population, growth rate, gestation period, and observation period answers
            try:
                i['answer'] = float(input(f"{i['question']}? "))
                # Check for input of 0 or negative numbers
                if i['answer'] <= 0:
                    print(i['error'])
                    exit()
            # Reject non-numerical responses
            except ValueError:
                print('Please enter a number.')
                continue
            break

    # Population object instantiation
    life_form = Population(data)
    # Simulate population growth
    life_form.simulate()


# Start program
if __name__ == '__main__':
    main()