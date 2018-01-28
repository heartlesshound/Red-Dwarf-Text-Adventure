worldRooms = {
	'Diesel Deck 1': {
		#Lister starts here
		DESC: 'Dark and grim',
		EXITN: 'Locked Door to Turbo Lift',
		EXITS: 'Diesel Deck 2',
		BEENHERE: 1
		}
	
	'Diesel Deck 2': {
		DESC: 'More dark and grim'
		EXITN: 'Diesel Deck 1',
		BEENHERE: 0,
		GROUND: ['Rimmers Broken Light Bee', 'Diesel Deck Access Card']
	}
		