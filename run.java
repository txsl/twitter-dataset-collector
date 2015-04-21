// package txl11;

import eu.socialsensor.twcollect.TweetCorpusDownloader;


public class run {
public static void main(String[] args)
    {
        if(args.length < 2){
            System.out.println("Not enough arguments passed in. Exiting.");
            System.exit(1);
        }
        else{
            System.out.println("Using input file " + args[0] + " and saving to " + args[1] + ".");
        }
        
        try{
            TweetCorpusDownloader.downloadIdsMultiThread(args[0], args[1], true, 10);
        }
        catch (Exception e){
            System.out.println(e.getMessage());
            System.exit(1);
        }
    }
}