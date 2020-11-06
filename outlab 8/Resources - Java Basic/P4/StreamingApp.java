/*
DO NOT MODIFY THE CODE STUB
NO NEED TO DEFINE main()
*/

import java.util.*;

class StreamingApp
{
	public static Map<String, ArrayList<String> > getFavouriteGenres(Map<String, ArrayList<String> > userMovies, Map<String, ArrayList<String> > movieGenres)
	{
		Map<String, ArrayList<String> > fav = new HashMap<>();
		Map<String, String> genre = new HashMap<>();
		for(Map.Entry<String, ArrayList<String>> m : movieGenres.entrySet()) {
			ArrayList<String> a = m.getValue();
			a.forEach((s) -> genre.put(s,m.getKey().toString()));
		}

		// for(Map.Entry<String,String> m : genre.entrySet()) {
		// 	System.out.println(m.getKey()+": "+ m.getValue());
		// }

		for(Map.Entry<String, ArrayList<String>> m: userMovies.entrySet()) {
			HashMap<String, Integer> hm = new HashMap<String, Integer>();
			ArrayList<String> top = new ArrayList<>();
			int max = 0; 
			for(int i=0; i < m.getValue().size(); i++) {
				String key = genre.get(m.getValue().get(i));
				if(hm.containsKey(key)) {
					int value = hm.get(key);
					value++;
					hm.put(key, value);
					if(value>max) {
						top = new ArrayList<>();
						top.add(key);
						max = value;
					} 
					else if(value == max) {
						top.add(key);
					}
				} else{
					hm.put(key, 1);
					if(max==0) {
						top = new ArrayList<>();
						top.add(key);
						max = 1;
					} else if(max==1) top.add(key);
				} 
			}
			fav.put(m.getKey(), top);
		}
		return fav;
	}
}