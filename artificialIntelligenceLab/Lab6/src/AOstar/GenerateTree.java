package AOstar;

import java.util.ArrayList;
import java.util.List;

public class GenerateTree {
	
	public static List<Integer> generateTree(){
		int noOfNodes;
		while((noOfNodes = (int)(Math.random()*10))<3);
		List<Integer> list = new ArrayList<Integer>();
		for(int i=0;i<noOfNodes;i++) {
			int temp;
			while((temp = (int)(Math.random()*100)) == 0);
			list.add(temp);
		}
		
		return list;
	}

}
