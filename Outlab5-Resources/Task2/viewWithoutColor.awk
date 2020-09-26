BEGIN {
	FS=","
	RS="\r\n"
}

(NR == 1 ){
	total = NF-1;
	
	for (i=1; i<NF; ++i){
		for (j=1; j<=20; ++j){
			printf("-")
		}
	}
	printf("\n")
	
	for (i=1; i<=NF; ++i){
		if (!match($i, "Name")){
			printf("%20s", $i)
		}
		else {
			remove = i
		}
	}
	printf("\n")
	for (i=1; i<NF; ++i){
		for (j=1; j<=20; ++j){
			printf("-")
		}
	}
	printf("\n")		
}
	

(NR != 1){
	for (i=1;i<=NF;++i){
		if (i!=remove){
			printf("%20s", $i)
		}
	}
	printf("\n")
}