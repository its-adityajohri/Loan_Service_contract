// SPDX-License-Identifier: MIT
pragma solidity >=0.4.25 <0.7.0;

// This is just a simple example of a coin-like contract.
// It is not standards compatible and cannot be expected to talk to other
// coin/token contracts. If you want to create a standards-compliant
// token, see: https://github.com/ConsenSys/Tokens. Cheers!

contract MetaCoin {
	mapping (address => uint256) balances;

	event Transfer(address indexed _from, address indexed _to, uint256 _value);

	constructor() public {
		balances[tx.origin] = 100000;
	}

	function sendCoin(address receiver, uint256 amount, address sender) public returns(bool sufficient) {
		if (balances[sender] < amount) return false;
		balances[sender] -= amount;
		balances[receiver] += amount;
		emit Transfer(sender, receiver, amount);
		return true;
	}


	function getBalance(address addr) public view returns(uint256) {
		return balances[addr];
	}
}

// Try not to edit the contract definition above

contract Loan is MetaCoin {
// You can edit this contract as much as you want. A template is provided here and you can change the function names and implement anything else you want, but the basic tasks mentioned here should be accomplished.
    mapping (address => uint256) private loans;
     
    event Request(address indexed _from, uint256 P, uint R, uint T, uint256 amt);
    
    address private Owner;

    address[] public addresses;




    
    modifier isOwner() {
        require(msg.sender == Owner);
        _;
        // Implement a modifier to allow only the owner of the contract to use specific functions
    }
    
    constructor() public {
        Owner = msg.sender;
        // Make the creator of the contract the Owner.
        // You can take the help of 2_owner.sol contract in remix for this and the above function. 
    }
    
    // Fill up the following function definitions and also try to justify why some functions are pure and some are view and some are none, in your README.md
    //function mulDiv (uint x, uint y, uint z) public pure returns (uint){
    //    return x * y / z;
    //}


    function getCompoundInterest(uint256 principle, uint rate, uint time) public pure returns(uint256) {
        uint256 R = rate;
        uint256 P = principle;
        while(time>0){
            P = P + R*P/100;
           time = time - 1;
        }
       // uint256 x = P - principle;
        return P;


    		// Anyone should be able to use this function to calculate the amount of Compound interest for given P, R, T
        // Solidity does not have a good support for fixed point numbers so we input the rate as a uint
        // A common way to perform division to calculate such percentages is mentioned here: 
        // https://medium.com/coinmonks/math-in-solidity-part-4-compound-interest-512d9e13041b just read the periodic compounding part and
        // https://medium.com/coinmonks/math-in-solidity-part-3-percents-and-proportions-4db014e080b1 just read the towards full proportion part.
        // A good way to prevent overflows will be to typecast principle, rate and the big number divider suggested in the above blogs as uint256 variables, just use uint256 R = rate;
        
    }
    
    function reqLoan(uint256 principle, uint rate, uint time) public returns(bool correct) {
        uint256 toPay = getCompoundInterest(principle, rate, time);

        loans[msg.sender]=toPay;
        if(loans[msg.sender]!=0){
        emit Request(owner,principle,rate,time,toPay);
        return true;
        }
        else{
            return false;
        // A creditor uses this function to request the Owner to settle his loan, and the amount to settle is calculated using the inputs.
        // Add appropriate definition below to store the loan request of a contract in the loans mapping,
        // Also emit the Request event after succesfully adding to the mapping, and return true. Return false if adding to the mapping failed (maybe the user entered a float rate, there were overflows and toPay comes to be lesser than principle, etc.
    }
    
    function getOwnerBalance() public view returns(uint256) {
        uint256 M = MetaCoin.getBalance(Owner);
        return M;

				// use the getBalance function of MetaCoin contract to view the Balance of the contract Owner.
				// hint: how do you access the functions / variables of the parent class in your favorite programming language? It is similar to that in solidity as well!
		}
    
    // implement viewDues and settleDues which allow *ONLY* the owner to *view* and *settle* his loans respectively. They take in the address of a creditor as arguments. viewDues returns a uint256 corresponding to the due amount, and does not modify any state variables. settleDues returns a bool, true if the dues were settled and false otherwise. Remember to set the the pending loan to 0 after settling the dues.
    // use sendCoin function of MetaCoin contract to send the coins required for settling the dues.
    function viewDues(address ad) public view isOwner returns(uint256){
        return (loans[ad]);
        //address[] memory Addresses = new address[](addresses.length);
        //uint[] memory Dues = new unit[](addresses.length);

        //for(uint i=0; i<addresses.lenth; i++){
            //Addresses[i] = addresses[i];
            //Dues[i] = loans[addresses[i]];
        //}

        //return(Addresses,Dues);
    }

    function settleDues(address ad) public isOwner returns(bool correct){
        bool b = MetaCoin.sendCoin(ad, loans[ad], address(this));
        if(b){
            loans[ad]=0;
            return true;
        }
        else{
            return false;
        }

    }
}