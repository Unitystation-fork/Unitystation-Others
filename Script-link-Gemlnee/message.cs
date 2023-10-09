using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

namespace MD_link_fixer
{
    class Program
    {
        static void Main(string[] args)
        {
            
            FixMDLinks();
            FixAssetsLinks();

            Console.WriteLine("Job's done.");
            Console.ReadKey();
        }

        private static void FixMDLinks()
        {

            string[] pathsToDocs = {
                "C:\\Users\\Geminee\\Documents\\GitHub\\Unitystation-WikiV2\\docs",
                "C:\\Users\\Geminee\\Documents\\GitHub\\Unitystation-WikiV2\\i18n\\DE\\docusaurus-plugin-content-docs\\current",
                "C:\\Users\\Geminee\\Documents\\GitHub\\Unitystation-WikiV2\\i18n\\FR\\docusaurus-plugin-content-docs\\current",
                "C:\\Users\\Geminee\\Documents\\GitHub\\Unitystation-WikiV2\\i18n\\RU\\docusaurus-plugin-content-docs\\current"
            };

            List<string> duplicates = new List<string>();
            List<string> filesNotFound = new List<string>();

            foreach (string path in pathsToDocs)
            {
                Dictionary<string, string> MDFiles = new Dictionary<string, string>();
                var filePathsToProcess = Directory.EnumerateFiles(path, "*.*", SearchOption.AllDirectories)
                    .Where(s => s.EndsWith(".md") || s.EndsWith(".mdx"));

                foreach (string filePath in filePathsToProcess)
                {
                    string fileName = Path.GetFileName(filePath);
                    string[] fileNameForSplit = { fileName };
                    string[] trimAbsolutePathPart = filePath.Split(pathsToDocs, StringSplitOptions.RemoveEmptyEntries);
                    string[] trimFileName = trimAbsolutePathPart[0].Split(fileNameForSplit, StringSplitOptions.RemoveEmptyEntries);

                    try
                    {
                        MDFiles.Add(fileName, trimFileName[0].Replace(@"\\", @"\"));
                    }
                    catch (Exception)
                    {
                        duplicates.Add(trimFileName[0].Replace(@"\\", @"\") + fileName);
                    }
                }

                Regex checkFileForMDLinkPattern = new Regex(@"\[[!'\.0-9a-zA-Z\s\-\(\)]*\]\([0-9a-zA-Z\s\.\\\-_]*\.md\)");

                foreach (string file in filePathsToProcess)
                {
                    StreamReader sr = new StreamReader(file);
                    string currentMD = sr.ReadToEnd();
                    sr.Close();

                    MatchCollection matchCollection = checkFileForMDLinkPattern.Matches(currentMD);

                    foreach (Match match in matchCollection)
                    {
                        Match currentMatch = match;
                        if (!currentMatch.Value.Contains("YOUTUBE") && !currentMatch.Value.Contains("http"))
                        {
                            string currentLink = currentMatch.Value;

                            bool isFileFounded = false;
                            foreach (KeyValuePair<string, string> kvp in MDFiles)
                            {
                                string key = kvp.Key;
                                if (currentLink.Contains(kvp.Key))
                                {
                                    isFileFounded = true;

                                    Regex linkNameRegex = new Regex(@"\(.*" + kvp.Key.Replace(@".", @"\.") + @"\)");
                                    string linkName = linkNameRegex.Replace(currentLink, @"");

                                    string newLink = linkName + "(" + kvp.Value + kvp.Key + ")";

                                    if (!currentLink.Equals(newLink))
                                    {
                                        currentMD = currentMD.Replace(currentLink, newLink);
                                    }

                                    break;
                                }
                            }

                            if (!isFileFounded)
                            {
                                isFileFounded = true;

                                string fileName = Path.GetFileName(file);
                                string[] fileNameForSplit = { fileName };
                                string[] trimAbsolutePathPart = file.Split(pathsToDocs, StringSplitOptions.RemoveEmptyEntries);
                                string[] trimFileName = trimAbsolutePathPart[0].Split(fileNameForSplit, StringSplitOptions.RemoveEmptyEntries);

                                filesNotFound.Add($"{currentLink} in {file}");  
                            }
                        }
                    }
                    StreamWriter sw = new StreamWriter(file);
                    sw.Write(currentMD);
                    sw.Close();
                }
            }

            StreamWriter swDuplicates = new StreamWriter("C:\\Users\\Geminee\\Documents\\GitHub\\Unitystation-WikiV2\\duplicates.txt");
            swDuplicates.WriteLine("Duplicates found:");
            foreach(string str in duplicates)
            {
                swDuplicates.WriteLine(str);
            }
            swDuplicates.Close();

            StreamWriter swFilesNotFound = new StreamWriter("C:\\Users\\Geminee\\Documents\\GitHub\\Unitystation-WikiV2\\FilesNotFound.txt");
            swFilesNotFound.WriteLine("Files not found:");
            foreach (string str in filesNotFound)
            {
                swFilesNotFound.WriteLine(str);
            }
            swFilesNotFound.Close();
        }

        private static void FixAssetsLinks()
        {

            #region Сбор ссылок на активы
            Dictionary<string, string> assetsFilesLinks = new Dictionary<string, string>();

            string basePathToStatic = "C:\\Users\\Geminee\\Documents\\GitHub\\Unitystation-WikiV2\\static";
            string[] delimiters = { "C:\\Users\\Geminee\\Documents\\GitHub\\Unitystation-WikiV2\\static" };
            string[] stings = Directory.GetFiles(basePathToStatic, "*.*", SearchOption.AllDirectories);

            foreach (string str in stings)
            {
                string fileName = Path.GetFileName(str);
                string[] fileNameForSplit = { fileName };
                string[] trimAbsolutePathPart = str.Split(delimiters, StringSplitOptions.RemoveEmptyEntries);
                string[] trimFileName = trimAbsolutePathPart[0].Split(fileNameForSplit, StringSplitOptions.RemoveEmptyEntries);

                try
                {
                    assetsFilesLinks.Add(fileName, trimFileName[0].Replace(@"\\", @"\"));
                }
                catch (Exception)
                {
                    //throw;
                }
            }

            #endregion

            Regex checkFileForLinkPattern = new Regex(@"!\[[!'\.0-9a-zA-Z\s\-\(\)]*\]\([0-9a-zA-Z\s\.\\\-_]*\)");
            // Regex linkIsCorrectMatch = new Regex(@"!\[\w*\]\(   \\asfasdf\\nweeee\.png  \)");
            // Regex linkHasFileName = new Regex(@"!\[[!'\.0-9a-zA-Z\s\-\(\)]*\]\(.*stack_objects_sheet-uranium\.png\)");

            string rootDirPath = "C:\\Users\\Geminee\\Documents\\GitHub\\Unitystation-WikiV2";

            string[] mdFilesAll = Directory.GetFiles(rootDirPath, "*.md", SearchOption.AllDirectories);
            string[] mdxFilesAll = Directory.GetFiles(rootDirPath, "*.mdx", SearchOption.AllDirectories);

            foreach (string md in mdFilesAll)
            {
                if (!md.Contains("node_modules"))
                {
                    StreamReader sr = new StreamReader(md);
                    string currentMD = sr.ReadToEnd();
                    sr.Close();

                    MatchCollection matchCollection = checkFileForLinkPattern.Matches(currentMD);

                    foreach (Match match in matchCollection)
                    {
                        Match currentMatch = match;
                        if (!currentMatch.Value.Contains("YOUTUBE") && !currentMatch.Value.Contains("http"))
                        {
                            string currentLink = currentMatch.Value;

                            bool isFileFounded = false;
                            foreach (KeyValuePair<string, string> kvp in assetsFilesLinks)
                            {
                                if (currentLink.Contains(kvp.Key))
                                {
                                    isFileFounded = true;

                                    Regex linkNameRegex = new Regex(@"\(.*" + kvp.Key.Replace(@".", @"\.") + @"\)");
                                    string linkName = linkNameRegex.Replace(currentLink, @"");

                                    string newLink = linkName + "(" + kvp.Value + kvp.Key + ")";

                                    if (!currentLink.Equals(newLink))
                                    {
                                        currentMD = currentMD.Replace(currentLink, newLink);
                                    }

                                    break;
                                }
                            }

                            if (!isFileFounded)
                            {
                                isFileFounded = true;

                                string newLink = @"\img\icon\No_image.png";

                                string fileName = "";
                                int foundClose = 0;
                                for (int i = currentLink.Length - 1; i > 0; i--)
                                {
                                    char currentChar = currentLink[i];
                                    if (currentChar == ')')
                                    {
                                        foundClose++;
                                    }
                                    else if (currentChar == '(')
                                    {
                                        foundClose--;
                                    }
                                    else if (i == currentLink.Length - 1 && currentChar != ')')
                                    {
                                        throw new Exception("incorrect file link");
                                    }
                                    if (foundClose == 0)
                                    {
                                        string[] pathSplitter = { "\\" };
                                        fileName = currentLink.Substring(i + 1, currentLink.Length - i - 2).Split(pathSplitter, StringSplitOptions.RemoveEmptyEntries).Last();
                                        break;
                                    }
                                }
                                Regex linkNameRegex = new Regex(@"\(.*" + fileName.Replace(@".", @"\.") + @"\)");
                                newLink = linkNameRegex.Replace(currentLink, @"(" + newLink + ")");

                                currentMD = currentMD.Replace(currentLink, newLink);
                            }
                        }
                    }
                    StreamWriter sw = new StreamWriter(md);
                    sw.Write(currentMD);
                    sw.Close();
                }
            }

            foreach (string mdx in mdxFilesAll)
            {
                if (!mdx.Contains("node_modules"))
                {
                    StreamReader sr = new StreamReader(mdx);
                    string currentMD = sr.ReadToEnd();

                    Match match = checkFileForLinkPattern.Match(currentMD);

                    sr.Close();
                }
            }
        }
    }
}
