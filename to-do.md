## Creating test plans

1. [ ] Create test plan
    *Product Dashboard -> Test Plans -> Create a new test plan*

## Creating test cases

2. [ ] Create test cases
    *Product Dashboard -> Test Cases -> Create new test cases*
    Test cases need to be associated with the test plan created in step 1.

## Adding build

3. [ ] Add build
    *Product Dashboard -> Builds -> Create new build*
    Build needs to be associated with the test plan created in step 1.

## Running test cases

4. [ ] Run test cases
    *Product Dashboard -> Test Runs -> Create a New Test run*
    Test run needs to be associated with the test plan created in step 1 and the test cases created in step 2.
    4.1 Select test plan *Test plan -> Use selected*
    4.2 Select test cases
    4.3 Input test parameters (if any) 
    4.4 Select result of the test run
    4.5 *Update Actions/Results*

## Bug reporting

5. [ ] Report bugs
    5.1 *Bugzilla - New*
    5.2 Input bug details, pay special attention to **Severity** parameter
    5.3 *Commit*

## Example

TEST PLAN: "Login Form Testing"
├── TEST CASE 1: "Log in with correct password"
├── TEST CASE 2: "Log in with incorrect password"
└── TEST CASE 3: "Leave password field empty"