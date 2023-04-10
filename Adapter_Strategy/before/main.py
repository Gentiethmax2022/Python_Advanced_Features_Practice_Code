import json 

from experiment import Experiment


def main() -> None:
    with open("C:\\Users\\genti\\OneDrive\\Desktop\\Python_Projects\\ArjanCodes\\Adapter_Strategy\\before\\config.json", encoding="utf8") as file:
        config = json.load(file)
        experiment = Experiment(config)
        experiment.run()
        

if __name__ == "__main__":
    main()
    
    