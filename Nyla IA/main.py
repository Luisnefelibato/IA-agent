from modules.data_collection import DataCollector
from modules.data_processing import DataProcessor
from modules.communication import Communicator
from modules.selection import TalentSelector
from modules.audition_management import AuditionManager

def main():
    # Initialize modules
    data_collector = DataCollector()
    data_processor = DataProcessor()
    communicator = Communicator()
    talent_selector = TalentSelector()
    audition_manager = AuditionManager()

    # Step 1: Data Collection
    raw_data = data_collector.collect_data()
    
    # Step 2: Data Processing
    processed_data = data_processor.process_data(raw_data)
    
    # Step 3: Initial Contact
    responses = communicator.contact_candidates(processed_data)
    
    # Step 4: Preselection
    selected_candidates = talent_selector.preselect_candidates(responses)
    
    # Step 5: Audition Management
    audition_manager.organize_auditions(selected_candidates)

if __name__ == "__main__":
    main()