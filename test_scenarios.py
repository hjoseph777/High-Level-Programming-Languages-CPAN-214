"""
Test Scenarios for Humber Bank Terminal
This script demonstrates all required testing scenarios from the instructions.

Author: Harry Joseph
Course: CPAN 214 - High-Level Programming Languages

This file simulates user inputs to test all the scenarios mentioned in instruction.md:
- 3 incorrect PIN attempts → program exits
- Correct PIN → access to menu
- Invalid menu choice → reprompt
- Balance check → shows accurate amount
- Withdraw $200 from $50 → "Insufficient funds"
- Deposit $30 → balance updates instantly
- Multiple actions in one session (deposit → withdraw → check balance → exit)
"""

import sys
from io import StringIO
from unittest.mock import patch
import humber_bank

def capture_output(inputs, description):
    """
    Helper function to capture program output with simulated inputs.
    This lets us test the program without manual interaction.
    """
    print(f"\n{'='*60}")
    print(f"TEST SCENARIO: {description}")
    print(f"{'='*60}")
    
    # Prepare the inputs as an iterator
    input_iter = iter(inputs)
    
    # Capture stdout
    captured_output = StringIO()
    
    with patch('builtins.input', side_effect=lambda prompt="": next(input_iter)):
        with patch('sys.stdout', captured_output):
            try:
                humber_bank.main()
            except StopIteration:
                # This happens when we run out of inputs - that's expected
                pass
    
    output = captured_output.getvalue()
    print("SIMULATED INPUTS:")
    for i, inp in enumerate(inputs, 1):
        print(f"  {i}. {inp}")
    
    print("\nPROGRAM OUTPUT:")
    print(output)
    return output

def run_all_test_scenarios():
    """
    Runs all the required test scenarios and captures their outputs.
    Each test demonstrates a different aspect of the program's functionality.
    """
    
    print("HUMBER BANK TERMINAL - COMPREHENSIVE TEST SUITE")
    print("=" * 60)
    print("Testing all scenarios required by the project instructions")
    
    # Scenario 1: 3 incorrect PIN attempts → program exits
    scenario1_inputs = ["1111", "2222", "3333"]  # All wrong PINs
    capture_output(scenario1_inputs, "3 Incorrect PIN Attempts - Should Exit")
    
    # Scenario 2: Correct PIN → access to menu (then exit immediately)
    scenario2_inputs = ["1234", "4"]  # Correct PIN, then exit
    capture_output(scenario2_inputs, "Correct PIN - Access Menu")
    
    # Scenario 3: Invalid menu choice → reprompt
    scenario3_inputs = ["1234", "9", "0", "abc", "4"]  # Correct PIN, invalid choices, then exit
    capture_output(scenario3_inputs, "Invalid Menu Choices - Should Reprompt")
    
    # Scenario 4: Balance check → shows accurate amount
    scenario4_inputs = ["1234", "1", "n"]  # Correct PIN, check balance, don't continue
    capture_output(scenario4_inputs, "Balance Check - Shows $1000.00")
    
    # Scenario 5: Withdraw more than available → "Insufficient funds"
    # First we need to check balance to see current amount, then try to withdraw more
    scenario5_inputs = ["1234", "2", "6", "1500", "n"]  # Try to withdraw $1500 from $1000
    capture_output(scenario5_inputs, "Insufficient Funds - Withdraw $1500 from $1000")
    
    # Scenario 6: Deposit $30 → balance updates instantly
    scenario6_inputs = ["1234", "3", "30", "n"]  # Deposit $30
    capture_output(scenario6_inputs, "Deposit $30 - Balance Should Update")
    
    # Scenario 7: Multiple actions in one session
    scenario7_inputs = [
        "1234",    # Correct PIN
        "3", "50", "y",      # Deposit $50, continue
        "2", "1", "y",       # Withdraw $20, continue  
        "1", "y",            # Check balance, continue
        "2", "6", "200", "y", # Try to withdraw $200 (should fail), continue
        "4"                  # Exit
    ]
    capture_output(scenario7_inputs, "Multiple Operations - Deposit, Withdraw, Check Balance, Failed Withdrawal, Exit")
    
    # Scenario 8: Test preset withdrawal amounts
    scenario8_inputs = ["1234", "2", "2", "n"]  # Withdraw $40 (preset option 2)
    capture_output(scenario8_inputs, "Preset Withdrawal - $40 (Option 2)")
    
    # Scenario 9: Test invalid deposit amounts
    scenario9_inputs = ["1234", "3", "-50", "0", "abc", "25", "n"]  # Invalid deposits, then valid $25
    capture_output(scenario9_inputs, "Invalid Deposit Amounts - Negative, Zero, Text, then Valid")

if __name__ == "__main__":
    run_all_test_scenarios()
    print("\n" + "="*60)
    print("ALL TEST SCENARIOS COMPLETED")
    print("="*60)
    print("\nReview the outputs above to verify all requirements are met:")
    print("✓ PIN verification with 3 attempts")
    print("✓ Menu access after correct PIN")
    print("✓ Input validation and error handling")
    print("✓ Balance checking and formatting")
    print("✓ Withdrawal validation (sufficient funds)")
    print("✓ Deposit functionality")
    print("✓ Multiple operations in one session")
    print("✓ Graceful exit messages")