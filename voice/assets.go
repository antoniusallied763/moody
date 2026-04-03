package voice

import (
	"embed"
	"io/fs"
	"os"
	"path/filepath"
)

//go:embed assets/*
var embeddedAssets embed.FS

// ExtractAssets copies the embedded audio files into the given packsDir
// if they don't already exist.
func ExtractAssets(packsDir string) error {
	return fs.WalkDir(embeddedAssets, "assets", func(path string, d fs.DirEntry, err error) error {
		if err != nil {
			return err
		}
		if d.IsDir() {
			return nil
		}

		// Calculate relative path inside 'assets'
		relPath, err := filepath.Rel("assets", path)
		if err != nil {
			return err
		}

		// Calculate destination path
		destPath := filepath.Join(packsDir, relPath)

		// Create directory if it doesn't exist
		if err := os.MkdirAll(filepath.Dir(destPath), 0755); err != nil {
			return err
		}

		// Check if file already exists
		if _, err := os.Stat(destPath); err == nil {
			return nil // File exists, skip
		}

		// Extract file
		data, err := embeddedAssets.ReadFile(path)
		if err != nil {
			return err
		}

		// Write to disk
		return os.WriteFile(destPath, data, 0644)
	})
}
