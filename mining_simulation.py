import random

#alpha: selfish miners mining power (percentage),
#gamma: the ratio of honest miners choose to mine on the selfish miners pool's block
#N: number of simulations run
def Simulate(alpha,gamma,N, seed):
	
	# DO NOT CHANGE. This is used to test your function despite randomness
	random.seed(seed)
  
	#the same as the state of the state machine in the slides 
	state=0
	# the length of the blockchain
	ChainLength=0
	# the revenue of the selfish mining pool
	SelfishRevenue=0
	# the number of hidden blocks
	HiddenBlock = 0

	#A round begin when the state=0
	for i in range(N):
		r=random.random()
		if state==0:
			#The selfish pool has 0 hidden block.
			if r<=alpha:
				#The selfish pool mines a block.
				#They don't publish it. 
				state=1
			else:
				#The honest miners found a block.
				#The round is finished : the honest miners found 1 block
				# and the selfish miners found 0 block.
				ChainLength+=1
				state=0

		elif state==1:
			#The selfish pool has 1 hidden block.
			HiddenBlock = 1
			if r<=alpha:
				#The selfish miners found a new block, but they dont publish it.
				state += 1
				HiddenBlock += 1
			else:
				#Others find a block and publish it, increasing the ChainLength by 1. 
				#The pool need to publish its hidden block. The state is 0'
				ChainLength += 1
				HiddenBlock = 0
				state = -1


		elif state==-1:
			#It's the state 0' in the slides (the paper of Eyal and Gun Sirer)
			#There are three situations! 
			#Write a piece of code to change the required variables in each one.
			if r<=alpha:
				#pool find a block after pool's lead, then they published 2 hidden blocks and get a revenue of 2
				ChainLength += 1
				SelfishRevenue += 2
				state = 0

			elif r<=alpha+(1-alpha)*gamma:
				#pool & others find a block after pool's lead, they both get a revenue of 1
				ChainLength += 1
				SelfishRevenue += 1
				state = 0

			else:
				#Others find a block after other's lead, others get a reveune of 2. 
				#the round is finished.
				ChainLength += 1
				state = 0

		elif state==2:
			#The selfish pool has 2 hidden block.
			if r<=alpha:
				#The selfish miners found a new block, but they dont publish it.
				state += 1
				HiddenBlock += 1
			else:
				#The honest miners found a block. Then the pool need to publish 2 of their hidden blocks to get a lead. 
				#pool minners get a revenue of 2, and this round is finished. 
				ChainLength += 2
				state = 0
				HiddenBlock = 0
				SelfishRevenue += 2

		elif state>2:
			if r<=alpha:
				#The selfish miners found a new block, they dont publish it.
				state += 1
				HiddenBlock += 1

			else:
				#The honest miners found a block
				#THe pool miners have to publish at least 1 blocks to keep the lead. The remaining HiddenBlock = (state-1)
				state -= 1
				HiddenBlock -= 1
				ChainLength += 1
				SelfishRevenue += 1


	return float(SelfishRevenue)/ChainLength


